---
{
  "projection_kind": "taulib_declaration",
  "title": "ext_gcd_fst",
  "permalink": "/verify/taulib/docs/book-i-polarity-ext-gcd/ext-gcd-fst/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.ExtGCD`.",
  "declaration_id": "TauLib.BookI.Polarity.ExtGCD::ext_gcd_fst",
  "declaration_slug": "ext-gcd-fst",
  "kind": "theorem",
  "name": "ext_gcd_fst",
  "module_name": "TauLib.BookI.Polarity.ExtGCD",
  "module_url": "/verify/taulib/docs/book-i-polarity-ext-gcd/",
  "source_line_start": 40,
  "source_line_end": 53,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/ExtGCD.lean#L40-L53",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.ExtGCD",
        "url": "/verify/taulib/docs/book-i-polarity-ext-gcd/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/ExtGCD.lean#L40-L53",
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

- Module: [TauLib.BookI.Polarity.ExtGCD](/verify/taulib/docs/book-i-polarity-ext-gcd/)
- Source path: [`TauLib/BookI/Polarity/ExtGCD.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/ExtGCD.lean#L40-L53)
- Source range: L40-L53
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- ext_gcd computes the GCD. -/
```

## Source Excerpt

```lean
theorem ext_gcd_fst (a b : Nat) : (ext_gcd a b).1 = Nat.gcd a b := by
  induction b using Nat.strongRecOn generalizing a with
  | _ b ih =>
  unfold ext_gcd
  split
  · -- b = 0
    rename_i hb; rw [hb, Nat.gcd_zero_right]
  · -- b > 0
    rename_i hb
    simp only []
    have hlt : a % b < b := Nat.mod_lt a (by omega)
    rw [ih (a % b) hlt b]
    -- Goal: Nat.gcd b (a % b) = Nat.gcd a b
    rw [Nat.gcd_comm a b, Nat.gcd_rec b a, Nat.gcd_comm]
```
