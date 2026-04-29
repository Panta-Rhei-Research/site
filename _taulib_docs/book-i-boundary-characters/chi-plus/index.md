---
{
  "projection_kind": "taulib_declaration",
  "title": "chi_plus",
  "permalink": "/verify/taulib/docs/book-i-boundary-characters/chi-plus/",
  "summary_short": "`def` declaration in `TauLib.BookI.Boundary.Characters`.",
  "declaration_id": "TauLib.BookI.Boundary.Characters::chi_plus",
  "declaration_slug": "chi-plus",
  "kind": "def",
  "name": "chi_plus",
  "module_name": "TauLib.BookI.Boundary.Characters",
  "module_url": "/verify/taulib/docs/book-i-boundary-characters/",
  "source_line_start": 48,
  "source_line_end": 49,
  "registry_ids": [
    "I.D37"
  ],
  "related_registry_items": [
    {
      "id": "I.D37",
      "title": "Lemniscate Characters",
      "url": "/registry/object/I.D37/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Characters.lean#L48-L49",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Characters.lean#L48-L49",
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

- Module: [TauLib.BookI.Boundary.Characters](/verify/taulib/docs/book-i-boundary-characters/)
- Source path: [`TauLib/BookI/Boundary/Characters.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Characters.lean#L48-L49)
- Source range: L48-L49
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `I.D37` — Lemniscate Characters

## Immediate Comment / Docstring

```lean
/-- [I.D37] The B-sector character χ₊: H_τ → Z, mapping a+bj ↦ a+b.
    As a SectorPair-valued map: projects to pure B-sector. -/
```

## Source Excerpt

```lean
def chi_plus (z : SplitComplex) : SectorPair :=
  ⟨z.re + z.im, 0⟩
```
