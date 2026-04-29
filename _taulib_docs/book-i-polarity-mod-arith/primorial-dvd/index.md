---
{
  "projection_kind": "taulib_declaration",
  "title": "primorial_dvd",
  "permalink": "/verify/taulib/docs/book-i-polarity-mod-arith/primorial-dvd/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.ModArith`.",
  "declaration_id": "TauLib.BookI.Polarity.ModArith::primorial_dvd",
  "declaration_slug": "primorial-dvd",
  "kind": "theorem",
  "name": "primorial_dvd",
  "module_name": "TauLib.BookI.Polarity.ModArith",
  "module_url": "/verify/taulib/docs/book-i-polarity-mod-arith/",
  "source_line_start": 156,
  "source_line_end": 169,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/ModArith.lean#L156-L169",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.ModArith",
        "url": "/verify/taulib/docs/book-i-polarity-mod-arith/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/verify/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/ModArith.lean#L156-L169",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
    }
  },
  "layout": "taulib-doc",
  "lane": "verify",
  "v2_lane": "verify",
  "status": "Canonical",
  "generated_from": "corpus/taulib-projections",
  "projection_version": "v0.1",
  "canonical_source": "Panta-Rhei-Research/taulib",
  "do_not_edit": true,
  "type": "TauLib Declaration"
}
---

## Declaration Projection

This page is generated directly from the pinned TauLib Lean source snapshot. The source excerpt is public because the active TauLib repository is public.

## Source Provenance

- Module: [TauLib.BookI.Polarity.ModArith](/verify/taulib/docs/book-i-polarity-mod-arith/)
- Source path: [`TauLib/BookI/Polarity/ModArith.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/ModArith.lean#L156-L169)
- Source range: L156-L169
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Primorial divisibility: M_k ∣ M_l when k ≤ l.
    This is the structural backbone of the inverse system. -/
```

## Source Excerpt

```lean
theorem primorial_dvd {k l : TauIdx} (h : k ≤ l) : primorial k ∣ primorial l := by
  induction l with
  | zero =>
    have : k = 0 := Nat.le_antisymm h (Nat.zero_le k)
    subst this; exact ⟨1, (Nat.mul_one _).symm⟩
  | succ l' ih =>
    simp only [TauIdx] at *
    by_cases hk : k = l' + 1
    · subst hk; exact ⟨1, (Nat.mul_one _).symm⟩
    · have hk' : k ≤ l' := by simp only [TauIdx] at *; omega
      obtain ⟨m, hm⟩ := ih hk'
      simp only [primorial]
      exact ⟨nth_prime (l' + 1) * m, by rw [hm, ← Nat.mul_assoc,
        Nat.mul_comm (nth_prime (l' + 1)) (primorial k), Nat.mul_assoc]⟩
```
