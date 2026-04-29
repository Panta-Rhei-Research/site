---
{
  "projection_kind": "taulib_declaration",
  "title": "StabilisedValue",
  "permalink": "/verify/taulib/docs/book-i-topos-circularity-resolution/stabilised-value/",
  "summary_short": "`inductive` declaration in `TauLib.BookI.Topos.CircularityResolution`.",
  "declaration_id": "TauLib.BookI.Topos.CircularityResolution::StabilisedValue",
  "declaration_slug": "stabilised-value",
  "kind": "inductive",
  "name": "StabilisedValue",
  "module_name": "TauLib.BookI.Topos.CircularityResolution",
  "module_url": "/verify/taulib/docs/book-i-topos-circularity-resolution/",
  "source_line_start": 186,
  "source_line_end": 195,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/CircularityResolution.lean#L186-L195",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Topos.CircularityResolution",
        "url": "/verify/taulib/docs/book-i-topos-circularity-resolution/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/CircularityResolution.lean#L186-L195",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "inductive",
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

- Module: [TauLib.BookI.Topos.CircularityResolution](/verify/taulib/docs/book-i-topos-circularity-resolution/)
- Source path: [`TauLib/BookI/Topos/CircularityResolution.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/CircularityResolution.lean#L186-L195)
- Source range: L186-L195
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The **ω-germ stabilised truth value** of a template at a seed,
    via the four-sector classification of the Cauchy iteration:

    - (a) eventually constant at `T` → stabilised value `T`
    - (b) eventually constant at `F` → stabilised value `F`
    - (c) period-2 oscillation between lobes → `B = Both = e_+ + e_-`
    - (d) none of the above → `N = Neither = 0`

    By the four-atom structure of `B_σ` (Hinge 4 uniqueness theorem)
    and the finite-state dynamics on the 4-element space `Truth4`,
    one of these four sectors always applies, but in general we
    have to allow more than one (e.g. an eventually-constant orbit
    is also "not period-2-on-lobes" only modulo a subtle witness
    budget; in this Lean rendering the sectors are stated as
    independent predicates and we do not enforce mutual exclusivity
    here). -/
```

## Source Excerpt

```lean
inductive StabilisedValue (Φ : Truth4 → Truth4) (s : Truth4) :
    Truth4 → Prop where
  | of_const_T : EventuallyConst Φ s T → StabilisedValue Φ s T
  | of_const_F : EventuallyConst Φ s F → StabilisedValue Φ s F
  | of_period2 : Period2OnLobes Φ s → StabilisedValue Φ s B
  | of_nonstab :
      ¬ EventuallyConst Φ s T →
      ¬ EventuallyConst Φ s F →
      ¬ Period2OnLobes Φ s →
      StabilisedValue Φ s N
```
