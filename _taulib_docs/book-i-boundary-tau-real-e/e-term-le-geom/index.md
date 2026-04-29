---
{
  "projection_kind": "taulib_declaration",
  "title": "TauRat.e_term_le_geom",
  "permalink": "/verify/taulib/docs/book-i-boundary-tau-real-e/e-term-le-geom/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.TauRealE`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRealE::TauRat.e_term_le_geom",
  "declaration_slug": "e-term-le-geom",
  "kind": "theorem",
  "name": "TauRat.e_term_le_geom",
  "module_name": "TauLib.BookI.Boundary.TauRealE",
  "module_url": "/verify/taulib/docs/book-i-boundary-tau-real-e/",
  "source_line_start": 76,
  "source_line_end": 91,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealE.lean#L76-L91",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.TauRealE",
        "url": "/verify/taulib/docs/book-i-boundary-tau-real-e/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealE.lean#L76-L91",
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

- Module: [TauLib.BookI.Boundary.TauRealE](/verify/taulib/docs/book-i-boundary-tau-real-e/)
- Source path: [`TauLib/BookI/Boundary/TauRealE.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealE.lean#L76-L91)
- Source range: L76-L91
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- `1/k! ≤ 1/2^(k−1)` for `k ≥ 1`, at the Rat level. -/
```

## Source Excerpt

```lean
theorem TauRat.e_term_le_geom (k : Nat) (hk : 1 ≤ k) :
    (TauRat.e_term k).toRat ≤ 1 / (2 ^ (k - 1) : Rat) := by
  rw [TauRat.e_term_toRat]
  have h_fact : (2 ^ (k - 1) : Nat) ≤ Nat.factorial k :=
    Nat.factorial_ge_two_pow k hk
  have h_fact_rat : ((2 : Rat) ^ (k - 1)) ≤ (Nat.factorial k : Rat) := by
    have h_cast : ((2 ^ (k - 1) : Nat) : Rat) ≤ (Nat.factorial k : Rat) := by
      exact_mod_cast h_fact
    have h_pow_cast : ((2 ^ (k - 1) : Nat) : Rat) = (2 : Rat) ^ (k - 1) := by
      push_cast; ring
    linarith
  have h_pos_pow : (0 : Rat) < 2 ^ (k - 1) := by positivity
  have h_pos_fact : (0 : Rat) < (Nat.factorial k : Rat) := by
    have := Nat.factorial_pos k; exact_mod_cast this
  rw [div_le_div_iff₀ h_pos_fact h_pos_pow]
  linarith
```
