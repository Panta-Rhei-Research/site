---
{
  "projection_kind": "taulib_declaration",
  "title": "Rat.one_div_two_n_lt_recip",
  "permalink": "/verify/taulib/docs/book-i-boundary-tau-real-pi/one-div-two-n-lt-recip/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.TauRealPi`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRealPi::Rat.one_div_two_n_lt_recip",
  "declaration_slug": "one-div-two-n-lt-recip",
  "kind": "theorem",
  "name": "Rat.one_div_two_n_lt_recip",
  "module_name": "TauLib.BookI.Boundary.TauRealPi",
  "module_url": "/verify/taulib/docs/book-i-boundary-tau-real-pi/",
  "source_line_start": 251,
  "source_line_end": 264,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealPi.lean#L251-L264",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.TauRealPi",
        "url": "/verify/taulib/docs/book-i-boundary-tau-real-pi/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealPi.lean#L251-L264",
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

- Module: [TauLib.BookI.Boundary.TauRealPi](/verify/taulib/docs/book-i-boundary-tau-real-pi/)
- Source path: [`TauLib/BookI/Boundary/TauRealPi.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealPi.lean#L251-L264)
- Source range: L251-L264
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- For `n ≥ k + 3`, we have `1/(2n) < 1/(k+1)`.  In fact `n ≥ k + 1`
    suffices, but `k + 3` matches Wave 3b's modulus shape. -/
```

## Source Excerpt

```lean
theorem Rat.one_div_two_n_lt_recip (k n : Nat) (hn : k + 3 ≤ n) :
    (1 : Rat) / (2 * (n : Rat)) < 1 / ((k : Rat) + 1) := by
  have h_n_pos : (0 : Rat) < (n : Rat) := by
    have : 1 ≤ n := by omega
    exact_mod_cast this
  have h_2n_pos : (0 : Rat) < 2 * (n : Rat) := by linarith
  have h_k1_pos : (0 : Rat) < (k : Rat) + 1 := by
    have : (0 : Rat) ≤ (k : Rat) := by exact_mod_cast Nat.zero_le k
    linarith
  rw [div_lt_div_iff₀ h_2n_pos h_k1_pos]
  -- Goal: (k+1) < 2n  for  n ≥ k+3
  have h_cast : ((k + 3 : Nat) : Rat) ≤ (n : Rat) := by exact_mod_cast hn
  have h_cast_eq : ((k + 3 : Nat) : Rat) = (k : Rat) + 3 := by push_cast; ring
  linarith
```
