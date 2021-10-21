# Modulo-Math-Tools
A set of tools for conveniently performing  common Modular Arithmetic. 

Many of these algorithms compute very important information for use in cryptography.

### Things I'd like to do (List may include more functions in the future):
- [X] Extended Euclidean Algorithm 
- [X] Implement Inverse
- [X] Fast Powers
- [X] Shanks' Algorithm
- [X] RSA key generation, encryption, and decryption
- [X] Random n-digit prime generation.
- [X] Miller-Rabin composite test
- [X] Seive of Eratosthenes.
- [ ] Downloadable package hosted on PyPi.
- [ ] Creation of Latex Code
- [ ] Intuitive GUI

To run, simply clone this github repo and cd to ./src/ and execute your commands here. An example of a command is:

`cd ./src/; python -c "import PyModulo; print("Inverse 3 ≡ %i (Mod 10)"%PyModulo.find_inverse(3,10))"`
