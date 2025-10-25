// src/firebase.js
import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";
import { getFirestore } from "firebase/firestore";

const firebaseConfig = {
  apiKey: "AIzaSyA270oiG2HO7UpaD-umY5d7_c08gJxRDGM",
  authDomain: "sdsd-469d7.firebaseapp.com",
  projectId: "sdsd-469d7",
  storageBucket: "sdsd-469d7.firebasestorage.app",
  messagingSenderId: "119202367667",
  appId: "1:119202367667:web:2f0dd9257005b5024a48c6"
};

const app = initializeApp(firebaseConfig);

export const auth = getAuth(app);
export const db = getFirestore(app);
