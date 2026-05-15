---
{
  "projection_kind": "taulib_declaration",
  "title": "TauRat.e_term",
  "permalink": "/corpus/taulib/docs/book-i-boundary-tau-real-e/e-term/",
  "summary_short": "`def` declaration in `TauLib.BookI.Boundary.TauRealE`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRealE::TauRat.e_term",
  "declaration_slug": "e-term",
  "kind": "def",
  "name": "TauRat.e_term",
  "module_name": "TauLib.BookI.Boundary.TauRealE",
  "module_url": "/corpus/taulib/docs/book-i-boundary-tau-real-e/",
  "source_line_start": 47,
  "source_line_end": 48,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealE.lean#L47-L48",
  "formal_status": "defined",
  "declaration_role": "data/computed value",
  "formal_status_label": "data/computed value",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.TauRealE",
        "url": "/corpus/taulib/docs/book-i-boundary-tau-real-e/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealE.lean#L47-L48",
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

- Module: [TauLib.BookI.Boundary.TauRealE](/corpus/taulib/docs/book-i-boundary-tau-real-e/)
- Source path: [`TauLib/BookI/Boundary/TauRealE.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealE.lean#L47-L48)
- Source range: L47-L48
- Kind: `def`
- Public role: `data/computed value`
- Formal status hint: `data/computed value`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The k-th term of the exponential series at 1: `1/k!`. -/
```

## Source Excerpt

```lean
def TauRat.e_term (k : Nat) : TauRat :=
  ⟨⟨1, 0⟩, Nat.factorial k, Nat.factorial_pos k⟩
```
