// Import the necessary Three.js modules
import * as THREE from 'three';

// Create a new scene, camera, and renderer
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer();

// Set the renderer size and add it to the HTML document
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

// Create a box geometry and material
const geometry = new THREE.BoxGeometry();
const material = new THREE.MeshBasicMaterial({ color: 0x00ff00 });

// Create a mesh by combining the geometry and material
const cube = new THREE.Mesh(geometry, material);

// Add the mesh to the scene
scene.add(cube);

// Set the camera position
camera.position.z = 5;

// Define an animation function that rotates the cube
function animate() {
  requestAnimationFrame(animate);
  cube.rotation.x += 0.01;
  cube.rotation.y += 0.01;
  renderer.render(scene, camera);
}

// Call the animation function to start the animation loop
animate();
