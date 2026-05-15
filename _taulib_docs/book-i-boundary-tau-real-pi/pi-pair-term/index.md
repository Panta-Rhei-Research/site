---
{
  "projection_kind": "taulib_declaration",
  "title": "TauRat.pi_pair_term",
  "permalink": "/corpus/taulib/docs/book-i-boundary-tau-real-pi/pi-pair-term/",
  "summary_short": "`def` declaration in `TauLib.BookI.Boundary.TauRealPi`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRealPi::TauRat.pi_pair_term",
  "declaration_slug": "pi-pair-term",
  "kind": "def",
  "name": "TauRat.pi_pair_term",
  "module_name": "TauLib.BookI.Boundary.TauRealPi",
  "module_url": "/corpus/taulib/docs/book-i-boundary-tau-real-pi/",
  "source_line_start": 70,
  "source_line_end": 71,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealPi.lean#L70-L71",
  "formal_status": "defined",
  "declaration_role": "data/computed value",
  "formal_status_label": "data/computed value",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.TauRealPi",
        "url": "/corpus/taulib/docs/book-i-boundary-tau-real-pi/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealPi.lean#L70-L71",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "data/computed value",
      "status": "data/computed value"
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

- Module: [TauLib.BookI.Boundary.TauRealPi](/corpus/taulib/docs/book-i-boundary-tau-real-pi/)
- Source path: [`TauLib/BookI/Boundary/TauRealPi.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealPi.lean#L70-L71)
- Source range: L70-L71
- Kind: `def`
- Public role: `data/computed value`
- Formal status hint: `data/computed value`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The k-th paired Leibniz term: `8 / ((4k+1)(4k+3))`. -/
```

## Source Excerpt

```lean
def TauRat.pi_pair_term (k : Nat) : TauRat :=
  ⟨⟨8, 0⟩, (4 * k + 1) * (4 * k + 3), by positivity⟩
```
