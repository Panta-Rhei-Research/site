---
{
  "projection_kind": "taulib_declaration",
  "title": "mod_mod_of_dvd",
  "permalink": "/verify/taulib/docs/book-i-polarity-mod-arith/mod-mod-of-dvd/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.ModArith`.",
  "declaration_id": "TauLib.BookI.Polarity.ModArith::mod_mod_of_dvd",
  "declaration_slug": "mod-mod-of-dvd",
  "kind": "theorem",
  "name": "mod_mod_of_dvd",
  "module_name": "TauLib.BookI.Polarity.ModArith",
  "module_url": "/verify/taulib/docs/book-i-polarity-mod-arith/",
  "source_line_start": 186,
  "source_line_end": 197,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/ModArith.lean#L186-L197",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/ModArith.lean#L186-L197",
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
- Source path: [`TauLib/BookI/Polarity/ModArith.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/ModArith.lean#L186-L197)
- Source range: L186-L197
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- If a ∣ b then (x % b) % a = x % a.
    Proved from first principles using Lean 4 core. -/
```

## Source Excerpt

```lean
theorem mod_mod_of_dvd (x a b : Nat) (h : a ∣ b) : x % b % a = x % a := by
  obtain ⟨c, rfl⟩ := h
  -- Goal: x % (a * c) % a = x % a
  -- Key decomposition: x = a * (c * q) + r where q = x/(a*c), r = x%(a*c)
  have hd : a * (c * (x / (a * c))) + x % (a * c) = x := by
    rw [← Nat.mul_assoc]; exact Nat.div_add_mod x (a * c)
  -- From mul_add_mod: (a * (c*q) + r) % a = r % a
  have hmul := mul_add_mod a (c * (x / (a * c))) (x % (a * c))
  -- Rewrite the LHS of hmul using hd: big expression → x
  rw [hd] at hmul
  -- hmul : x % a = (x % (a * c)) % a
  exact hmul.symm
```
