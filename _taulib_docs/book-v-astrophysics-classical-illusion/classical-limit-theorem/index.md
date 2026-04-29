---
{
  "projection_kind": "taulib_declaration",
  "title": "classical_limit_theorem",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-classical-illusion/classical-limit-theorem/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.ClassicalIllusion`.",
  "declaration_id": "TauLib.BookV.Astrophysics.ClassicalIllusion::classical_limit_theorem",
  "declaration_slug": "classical-limit-theorem",
  "kind": "theorem",
  "name": "classical_limit_theorem",
  "module_name": "TauLib.BookV.Astrophysics.ClassicalIllusion",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-classical-illusion/",
  "source_line_start": 123,
  "source_line_end": 125,
  "registry_ids": [
    "V.T78"
  ],
  "related_registry_items": [
    {
      "id": "V.T78",
      "title": "Newtonian Limit --- V.T30",
      "url": "/registry/object/V.T78/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/ClassicalIllusion.lean#L123-L125",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.ClassicalIllusion",
        "url": "/verify/taulib/docs/book-v-astrophysics-classical-illusion/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/ClassicalIllusion.lean#L123-L125",
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

- Module: [TauLib.BookV.Astrophysics.ClassicalIllusion](/verify/taulib/docs/book-v-astrophysics-classical-illusion/)
- Source path: [`TauLib/BookV/Astrophysics/ClassicalIllusion.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/ClassicalIllusion.lean#L123-L125)
- Source range: L123-L125
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T78` — Newtonian Limit --- V.T30

## Immediate Comment / Docstring

```lean
/-- [V.T78] Classical limit theorem: in the regime where fiber modes
    are frozen and D-sector dominates, the τ-equations reduce to
    Newton's F = ma.

    The theorem is structural: the three conditions (continuum limit,
    ground-state fiber, D-sector dominance) together force the
    Euler-Lagrange equations of classical mechanics. -/
```

## Source Excerpt

```lean
theorem classical_limit_theorem (m : ClassicalReadoutMap)
    (hf : m.fiber_frozen = true) (hr : m.regime = .Newtonian) :
    m.fiber_frozen = true ∧ m.regime = .Newtonian := ⟨hf, hr⟩
```
