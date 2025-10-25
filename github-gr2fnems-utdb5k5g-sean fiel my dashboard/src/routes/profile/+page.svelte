<script>
  import { goto } from "$app/navigation";
  import { auth, db } from "../../firebase";
  import { doc, getDoc, setDoc } from "firebase/firestore";
  import { onAuthStateChanged } from "firebase/auth";
  import Navbar from "$lib/Navbar.svelte";

  let email = "";
  let displayName = "";
  let bio = "";
  let hobby = "";
  let user = null;

  // Load user + Firestore data
  onAuthStateChanged(auth, async (u) => {
    if (u) {
      user = u;
      email = u.email;
      displayName = u.displayName || "";

      // Load Firestore profile
      const ref = doc(db, "users", u.uid);
      const snap = await getDoc(ref);
      if (snap.exists()) {
        const data = snap.data();
        bio = data.bio || "";
        hobby = data.hobby || "";
      }
    }
  });

  // Save profile data
  async function saveProfile() {
    if (!user) return;

    try {
      const ref = doc(db, "users", user.uid);
      await setDoc(ref, { bio, hobby }, { merge: true });
      alert("Profile updated!");
    } catch (err) {
      console.error(err);
      alert("Error saving profile: " + err.message);
    }
  }
</script>

<svelte:head>
  <title>Profile Settings</title>
  <link 
    href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" 
    rel="stylesheet"
  >
  <link 
    href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.0/font/bootstrap-icons.css" 
    rel="stylesheet"
  >
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</svelte:head>

<Navbar />

<div class="container py-4">
  <div class="card shadow-sm p-4">
    <h3 class="mb-3">Profile Settings</h3>

    <div class="mb-3">
      <label class="form-label">Email Address</label>
      <input class="form-control" type="email" value={email} disabled />
    </div>

    <div class="mb-3">
      <label class="form-label">Favorite Hobby</label>
      <input
        class="form-control"
        type="text"
        bind:value={hobby}
        placeholder="Enter your hobby"
      />
    </div>

    <div class="mb-3">
      <label class="form-label">Bio</label>
      <textarea
        class="form-control"
        rows="3"
        bind:value={bio}
        placeholder="Tell us about yourself..."
      ></textarea>
    </div>

    <button class="btn btn-primary" on:click={saveProfile}>
      Save Changes
    </button>
    <button class="btn btn-secondary ms-2" on:click={() => history.back()}>
      ← Back
    </button>
  </div>
</div>