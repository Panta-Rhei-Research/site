---
{
  "projection_kind": "taulib_declaration",
  "title": "chi_complete",
  "permalink": "/verify/taulib/docs/book-i-boundary-characters/chi-complete/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.Characters`.",
  "declaration_id": "TauLib.BookI.Boundary.Characters::chi_complete",
  "declaration_slug": "chi-complete",
  "kind": "theorem",
  "name": "chi_complete",
  "module_name": "TauLib.BookI.Boundary.Characters",
  "module_url": "/verify/taulib/docs/book-i-boundary-characters/",
  "source_line_start": 148,
  "source_line_end": 151,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Characters.lean#L148-L151",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Characters.lean#L148-L151",
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
- Source path: [`TauLib/BookI/Boundary/Characters.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Characters.lean#L148-L151)
- Source range: L148-L151
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `I.D38` — Character Group

## Immediate Comment / Docstring

```lean
/-- [I.D38] Completeness: χ₊(z) + χ₋(z) = to_sectors(z).
    The two characters together reconstruct the full sector decomposition. -/
```

## Source Excerpt

```lean
theorem chi_complete (z : SplitComplex) :
    SectorPair.add (chi_plus z) (chi_minus z) = to_sectors z := by
  simp only [chi_plus, chi_minus, SectorPair.add, to_sectors, SectorPair.mk.injEq]
  constructor <;> omega
```
