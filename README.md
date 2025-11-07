[![MRP](https://img.shields.io/github/stars/eneamazzoni/MRP?style=social)](https://github.com/eneamazzoni/MRP)

# MRP – Mazzoni Recovery Protocol
> **Any public text + one mental rule = 24, 48, or 72 BIP39 words — all in your head.**
**One protocol. One sentence. Infinite entropy.**

---
## Core Protocol
1. **Choose any stable public text**
2. **Define one mental rule** (in your head only)
3. **Extract 24, 48, or 72 words** → map to BIP39
4. **Enter into Ledger**

→ **No backup. No risk. Just you + literature.**

---
## Memory Rule (applies to all)
> **"Gandalf, Bilbo, Winston: after each chapter, take the first noun."**

→ **One sentence = 72 words in your head.**

---
## Survival Seed
> **Shipwrecked, refugee, seizure —  
> if you remember the rule, you rebuild everything.**

---
## Examples

### 1. Beginner (24 words)
- **Text**: LOTR (HarperCollins 2004)
- **Rule**: 1st common noun per chapter
- **Output**: see [`lotr_2004.csv`](lotr_2004.csv)
- **Entropy**: ~80 bit

### 2. Advanced (24 words)
- **Text**: 3 books × 8 chapters
- **Rule**: see [`rule_variants.md`](rule_variants.md)
- **Entropy**: ~256 bit

### 3. Whale (48 words)
- **Text**: LOTR + Hobbit (1–24 each)
- **Rule**: 1st common noun per chapter
- **Entropy**: ~528 bit

### 4. Quantum (72 words)
- **Text**: LOTR + Hobbit + 1984 (1–24 each)
- **Rule**: 1st common noun per chapter
- **Entropy**: **792 bit**

---
## MRP 2-of-2: Mental Multi-Signature
> **Book (Person A) + Rule (Person B) = Seed**  
> **Neither can recover alone.**

### How it works
- **Person A** knows **only the public text** (e.g. "LOTR HarperCollins 2004")
- **Person B** knows **only the mental rule** (e.g. "1st noun after 'the'")
- Both must **collaborate** to reconstruct the 24-word BIP39 seed

### Use Cases
| Scenario | A (Book) | B (Rule) |
|--------|---------|---------|
| Family Office | Parent | Child |
| Hedge Fund | Trader | Compliance |
| DAO | Member 1 | Member 2 |
| Inheritance | You | Notary |

### Security
- **Zero hardware**
- **Zero shared backup**
- **$5 wrench resistant**
- **Same entropy as standard 24-word seed**

> **True trustless 2-of-2 — powered by literature and the human mind.**

---
## Tools & Templates
| File | Use |
|------|-----|
| [`lotr_2004.csv`](lotr_2004.csv) | Full 22-word list from LOTR (Example 1) |
| [`rule_variants.md`](rule_variants.md) | 10 mental rule ideas |
| [`mapper.py`](mapper.py) | Auto-map non-BIP39 words to BIP39 |
| [`notary_template.txt`](notary_template.txt) | Swiss notary letter (post-mortem access) |

---
## Security
- Book = public
- Rule = private (mental)
- Notary = legal trigger

> **24 words = 256 bit**  
> **48 words = 528 bit**  
> **72 words = 792 bit**  
> **MRP = 24/48/72 words that live only in your head.**

---
## Security Comparison
| Method | Entropy | Attack Surface | Human Error | Resilience | Inheritance | Portability |
|--------|---------|----------------|-------------|------------|-------------|-------------|
| Paper/Metal | 256 bit | Physical | High | Low | Easy | Low |
| Cloud | 256 bit | Online | Medium | Medium | Hard | High |
| Brainwallet | 256 bit | Social | High | High | Hard | Max |
| **MRP 24** | **256 bit** | **Zero** | **Low** | **Max** | **Easy** | **Max** |
| **MRP 48** | **528 bit** | **Zero** | **Low** | **Max** | **Easy** | **Max** |
| **MRP 72** | **792 bit** | **Zero** | **Low** | **Max** | **Easy** | **Max** |

> **MRP = the only method with zero attack surface and max resilience.**

---
## License
MIT © 2025 Enea Mazzoni (@eneamazzoni)

---
## License
MIT © 2025 Enea Mazzoni (@eneamazzoni)
