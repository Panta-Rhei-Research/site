---
{
  "projection_kind": "taulib_declaration",
  "title": "TauRat.factorial",
  "permalink": "/verify/taulib/docs/book-i-boundary-tau-real-sum/factorial/",
  "summary_short": "`def` declaration in `TauLib.BookI.Boundary.TauRealSum`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRealSum::TauRat.factorial",
  "declaration_slug": "factorial",
  "kind": "def",
  "name": "TauRat.factorial",
  "module_name": "TauLib.BookI.Boundary.TauRealSum",
  "module_url": "/verify/taulib/docs/book-i-boundary-tau-real-sum/",
  "source_line_start": 57,
  "source_line_end": 58,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealSum.lean#L57-L58",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.TauRealSum",
        "url": "/verify/taulib/docs/book-i-boundary-tau-real-sum/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealSum.lean#L57-L58",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "status": "defined"
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

- Module: [TauLib.BookI.Boundary.TauRealSum](/verify/taulib/docs/book-i-boundary-tau-real-sum/)
- Source path: [`TauLib/BookI/Boundary/TauRealSum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealSum.lean#L57-L58)
- Source range: L57-L58
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Rational factorial: `TauRat.factorial n = n!` as a `TauRat`.
    Built via Lean core's `Nat.factorial`. -/
```

## Source Excerpt

```lean
def TauRat.factorial (n : Nat) : TauRat :=
  ⟨⟨Nat.factorial n, 0⟩, 1, Nat.one_pos⟩
```
