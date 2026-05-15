---
{
  "projection_kind": "taulib_declaration",
  "title": "chi_plus_neg",
  "permalink": "/corpus/taulib/docs/book-i-boundary-characters/chi-plus-neg/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.Characters`.",
  "declaration_id": "TauLib.BookI.Boundary.Characters::chi_plus_neg",
  "declaration_slug": "chi-plus-neg",
  "kind": "theorem",
  "name": "chi_plus_neg",
  "module_name": "TauLib.BookI.Boundary.Characters",
  "module_url": "/corpus/taulib/docs/book-i-boundary-characters/",
  "source_line_start": 101,
  "source_line_end": 104,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Characters.lean#L101-L104",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.Characters",
        "url": "/corpus/taulib/docs/book-i-boundary-characters/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Characters.lean#L101-L104",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookI.Boundary.Characters](/corpus/taulib/docs/book-i-boundary-characters/)
- Source path: [`TauLib/BookI/Boundary/Characters.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Characters.lean#L101-L104)
- Source range: L101-L104
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- χ₊ preserves negation. -/
```

## Source Excerpt

```lean
theorem chi_plus_neg (z : SplitComplex) :
    chi_plus (SplitComplex.neg z) = SectorPair.neg (chi_plus z) := by
  simp only [chi_plus, SplitComplex.neg, SectorPair.neg, SectorPair.mk.injEq]
  constructor <;> ring
```
