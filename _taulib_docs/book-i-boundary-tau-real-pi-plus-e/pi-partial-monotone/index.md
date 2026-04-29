---
{
  "projection_kind": "taulib_declaration",
  "title": "TauRat.pi_partial_monotone",
  "permalink": "/verify/taulib/docs/book-i-boundary-tau-real-pi-plus-e/pi-partial-monotone/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.TauRealPiPlusE`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRealPiPlusE::TauRat.pi_partial_monotone",
  "declaration_slug": "pi-partial-monotone",
  "kind": "theorem",
  "name": "TauRat.pi_partial_monotone",
  "module_name": "TauLib.BookI.Boundary.TauRealPiPlusE",
  "module_url": "/verify/taulib/docs/book-i-boundary-tau-real-pi-plus-e/",
  "source_line_start": 56,
  "source_line_end": 74,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealPiPlusE.lean#L56-L74",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.TauRealPiPlusE",
        "url": "/verify/taulib/docs/book-i-boundary-tau-real-pi-plus-e/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealPiPlusE.lean#L56-L74",
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

- Module: [TauLib.BookI.Boundary.TauRealPiPlusE](/verify/taulib/docs/book-i-boundary-tau-real-pi-plus-e/)
- Source path: [`TauLib/BookI/Boundary/TauRealPiPlusE.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealPiPlusE.lean#L56-L74)
- Source range: L56-L74
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- `pi_partial` is monotone increasing at the `toRat` level. -/
```

## Source Excerpt

```lean
theorem TauRat.pi_partial_monotone {m n : Nat} (hmn : m ≤ n) :
    (TauRat.pi_partial m).toRat ≤ (TauRat.pi_partial n).toRat := by
  induction n with
  | zero =>
    have : m = 0 := by omega
    subst this
    exact _root_.le_refl _
  | succ n ih =>
    by_cases h : m = n + 1
    · subst h; exact _root_.le_refl _
    · have hmn' : m ≤ n := by omega
      have ih' := ih hmn'
      have h_succ : TauRat.pi_partial (n + 1) =
                    (TauRat.pi_partial n).add (TauRat.pi_pair_term n) := by
        show TauRat.sum TauRat.pi_pair_term (n + 1) = _
        rfl
      rw [h_succ, toRat_add]
      have h_pos := _root_.le_of_lt (TauRat.pi_pair_term_pos n)
      linarith
```
