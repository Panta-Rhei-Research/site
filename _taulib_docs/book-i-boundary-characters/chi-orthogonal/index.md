---
{
  "projection_kind": "taulib_declaration",
  "title": "chi_orthogonal",
  "permalink": "/verify/taulib/docs/book-i-boundary-characters/chi-orthogonal/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.Characters`.",
  "declaration_id": "TauLib.BookI.Boundary.Characters::chi_orthogonal",
  "declaration_slug": "chi-orthogonal",
  "kind": "theorem",
  "name": "chi_orthogonal",
  "module_name": "TauLib.BookI.Boundary.Characters",
  "module_url": "/verify/taulib/docs/book-i-boundary-characters/",
  "source_line_start": 164,
  "source_line_end": 166,
  "registry_ids": [
    "I.D38"
  ],
  "related_registry_items": [
    {
      "id": "I.D38",
      "title": "Character Group",
      "url": "/registry/object/I.D38/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Characters.lean#L164-L166",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.Characters",
        "url": "/verify/taulib/docs/book-i-boundary-characters/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Characters.lean#L164-L166",
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

- Module: [TauLib.BookI.Boundary.Characters](/verify/taulib/docs/book-i-boundary-characters/)
- Source path: [`TauLib/BookI/Boundary/Characters.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Characters.lean#L164-L166)
- Source range: L164-L166
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `I.D38` — Character Group

## Immediate Comment / Docstring

```lean
/-- [I.D38] Orthogonality: χ₊(z) · χ₋(w) = 0 for all z, w.
    The B-sector and C-sector are mutually annihilating. -/
```

## Source Excerpt

```lean
theorem chi_orthogonal (z w : SplitComplex) :
    SectorPair.mul (chi_plus z) (chi_minus w) = SectorPair.zero := by
  simp [chi_plus, chi_minus, SectorPair.mul, SectorPair.zero]
```
