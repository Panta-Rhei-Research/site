---
{
  "projection_kind": "taulib_declaration",
  "title": "TauRat.pi_pair_term_pos",
  "permalink": "/verify/taulib/docs/book-i-boundary-tau-real-pi/pi-pair-term-pos/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.TauRealPi`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRealPi::TauRat.pi_pair_term_pos",
  "declaration_slug": "pi-pair-term-pos",
  "kind": "theorem",
  "name": "TauRat.pi_pair_term_pos",
  "module_name": "TauLib.BookI.Boundary.TauRealPi",
  "module_url": "/verify/taulib/docs/book-i-boundary-tau-real-pi/",
  "source_line_start": 78,
  "source_line_end": 83,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealPi.lean#L78-L83",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealPi.lean#L78-L83",
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
- Source path: [`TauLib/BookI/Boundary/TauRealPi.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealPi.lean#L78-L83)
- Source range: L78-L83
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
No immediate Lean doc/comment block was detected for this declaration.
```

## Source Excerpt

```lean
theorem TauRat.pi_pair_term_pos (k : Nat) : 0 < (TauRat.pi_pair_term k).toRat := by
  rw [TauRat.pi_pair_term_toRat]
  have h_pos : (0 : Rat) < (((4 * k + 1) * (4 * k + 3) : Nat) : Rat) := by
    have : 0 < (4 * k + 1) * (4 * k + 3) := by positivity
    exact_mod_cast this
  exact div_pos (by norm_num) h_pos
```
