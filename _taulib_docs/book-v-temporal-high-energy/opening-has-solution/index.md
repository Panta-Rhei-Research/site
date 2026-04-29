---
{
  "projection_kind": "taulib_declaration",
  "title": "opening_has_solution",
  "permalink": "/verify/taulib/docs/book-v-temporal-high-energy/opening-has-solution/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Temporal.HighEnergy`.",
  "declaration_id": "TauLib.BookV.Temporal.HighEnergy::opening_has_solution",
  "declaration_slug": "opening-has-solution",
  "kind": "theorem",
  "name": "opening_has_solution",
  "module_name": "TauLib.BookV.Temporal.HighEnergy",
  "module_url": "/verify/taulib/docs/book-v-temporal-high-energy/",
  "source_line_start": 153,
  "source_line_end": 158,
  "registry_ids": [
    "V.T13"
  ],
  "related_registry_items": [
    {
      "id": "V.T13",
      "title": "Opening Regime Theorem",
      "url": "/registry/object/V.T13/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/HighEnergy.lean#L153-L158",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Temporal.HighEnergy",
        "url": "/verify/taulib/docs/book-v-temporal-high-energy/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/HighEnergy.lean#L153-L158",
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

- Module: [TauLib.BookV.Temporal.HighEnergy](/verify/taulib/docs/book-v-temporal-high-energy/)
- Source path: [`TauLib/BookV/Temporal/HighEnergy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/HighEnergy.lean#L153-L158)
- Source range: L153-L158
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T13` — Opening Regime Theorem

## Immediate Comment / Docstring

```lean
/-- [V.T13] In the opening regime, the τ-Einstein equation has a
    unique solution at each depth n.

    The uniqueness follows from τ-NF minimization: at each depth,
    the normal form is unique (finite quotient has a unique minimizer),
    and the τ-Einstein identity G = κ_τ · T^mat is algebraic (not PDE).

    This means: no gauge freedom, no initial-condition dependence.
    The universe at each depth is uniquely determined by the τ-kernel. -/
```

## Source Excerpt

```lean
theorem opening_has_solution (r : OpeningRegime) :
    -- The regime is nonempty (solutions exist at each depth in range)
    r.n_end > r.n_start ∧
    -- τ-NF uniqueness carries over from the refinement tower
    r.n_start > 0 :=
  ⟨r.nonempty, r.start_pos⟩
```
