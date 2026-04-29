---
{
  "projection_kind": "taulib_declaration",
  "title": "ReadoutAnchor",
  "permalink": "/verify/taulib/docs/book-iv-physics-readout-functor/readout-anchor/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Physics.ReadoutFunctor`.",
  "declaration_id": "TauLib.BookIV.Physics.ReadoutFunctor::ReadoutAnchor",
  "declaration_slug": "readout-anchor",
  "kind": "structure",
  "name": "ReadoutAnchor",
  "module_name": "TauLib.BookIV.Physics.ReadoutFunctor",
  "module_url": "/verify/taulib/docs/book-iv-physics-readout-functor/",
  "source_line_start": 137,
  "source_line_end": 148,
  "registry_ids": [
    "IV.D327"
  ],
  "related_registry_items": [
    {
      "id": "IV.D327",
      "title": "Readout Anchor",
      "url": "/registry/object/IV.D327/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/ReadoutFunctor.lean#L137-L148",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Physics.ReadoutFunctor",
        "url": "/verify/taulib/docs/book-iv-physics-readout-functor/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/ReadoutFunctor.lean#L137-L148",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
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

- Module: [TauLib.BookIV.Physics.ReadoutFunctor](/verify/taulib/docs/book-iv-physics-readout-functor/)
- Source path: [`TauLib/BookIV/Physics/ReadoutFunctor.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/ReadoutFunctor.lean#L137-L148)
- Source range: L137-L148
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D327` — Readout Anchor

## Immediate Comment / Docstring

```lean
/-- [IV.D327] The calibration anchor: the single empirical input
    to the readout functor.

    In the τ-framework, m_n (neutron mass) is the unique anchor because:
    1. The neutron is the first ontic particle (minimal mass-bearing config)
    2. It is directly measurable (Penning trap)
    3. All other masses are internal ratios times m_n
    4. All other dimensionful constants factor through m_n + exact SI -/
```

## Source Excerpt

```lean
structure ReadoutAnchor where
  /-- The SI constant serving as anchor. -/
  anchor : SIConstant
  /-- The anchor quantity is Mass. -/
  quantity : PrimaryInvariant
  /-- It is a mass measurement. -/
  is_mass : quantity = .Mass
  /-- The measurement procedure. -/
  procedure : MeasurementProcedure
  /-- The procedure is flagged as anchor. -/
  procedure_is_anchor : procedure.is_anchor = true
  deriving Repr
```
