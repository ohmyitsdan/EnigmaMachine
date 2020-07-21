# Enigma Machine

> An Enigma substitution cipher machine based on the German 1930's and future models, used in WW2.

> enigma, cipher, encoding, cryptography

---

**Future Updates:**

- Include options for plug board
- Create starting points for each rotor
- Create GUI

---

## Usage

1. Create an Enigma object, there are a choice of 3 reflectors, and 5 rotors. Rotors 1-3 are mandatory, 4-5 are option and require keywords 'pos4' and 'pos5'.

```python
e = Enigma('reflectorB', 'rotor3', 'rotor1', 'rotor5', pos4='rotor4')
```

Then simply encode the phrase you want.

```
e.encode('Hello World')
```

and out comes the encoded phrase, which can, under the correct settings be input and decoded.

```
'PGVMQ UMPNU'
```

## License
