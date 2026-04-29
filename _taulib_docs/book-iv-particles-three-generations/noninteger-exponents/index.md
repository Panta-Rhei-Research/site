---
{
  "projection_kind": "taulib_declaration",
  "title": "noninteger_exponents",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/noninteger-exponents/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::noninteger_exponents",
  "declaration_slug": "noninteger-exponents",
  "kind": "def",
  "name": "noninteger_exponents",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 354,
  "source_line_end": 355,
  "registry_ids": [
    "IV.R114"
  ],
  "related_registry_items": [
    {
      "id": "IV.R114",
      "title": "Non-integer exponents are physical",
      "url": "/registry/object/IV.R114/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L354-L355",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Particles.ThreeGenerations",
        "url": "/verify/taulib/docs/book-iv-particles-three-generations/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L354-L355",
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

- Module: [TauLib.BookIV.Particles.ThreeGenerations](/verify/taulib/docs/book-iv-particles-three-generations/)
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L354-L355)
- Source range: L354-L355
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.R114` — Non-integer exponents are physical

## Immediate Comment / Docstring

```lean
/-- [IV.R114] Generation exponents are not exact integers: bare
    topological values (5 for muon, 15/2 for tau) are shifted by
    EM radiative corrections of order α ≈ 1/137. -/
```

## Source Excerpt

```lean
def noninteger_exponents : String :=
  "Bare exponents shifted by O(alpha) radiative corrections"
```
