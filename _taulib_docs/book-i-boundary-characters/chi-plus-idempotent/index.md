---
{
  "projection_kind": "taulib_declaration",
  "title": "chi_plus_idempotent",
  "permalink": "/verify/taulib/docs/book-i-boundary-characters/chi-plus-idempotent/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.Characters`.",
  "declaration_id": "TauLib.BookI.Boundary.Characters::chi_plus_idempotent",
  "declaration_slug": "chi-plus-idempotent",
  "kind": "theorem",
  "name": "chi_plus_idempotent",
  "module_name": "TauLib.BookI.Boundary.Characters",
  "module_url": "/verify/taulib/docs/book-i-boundary-characters/",
  "source_line_start": 178,
  "source_line_end": 181,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Characters.lean#L178-L181",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Characters.lean#L178-L181",
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
- Source path: [`TauLib/BookI/Boundary/Characters.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Characters.lean#L178-L181)
- Source range: L178-L181
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- χ₊ is an idempotent projection: χ₊² = χ₊ (in the sector ring). -/
```

## Source Excerpt

```lean
theorem chi_plus_idempotent (z : SplitComplex) :
    SectorPair.mul (chi_plus z) (chi_plus z) =
    ⟨(z.re + z.im) * (z.re + z.im), 0⟩ := by
  simp [chi_plus, SectorPair.mul]
```
