---
{
  "projection_kind": "taulib_declaration",
  "title": "CosmicPhase",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cosmological-endstate/cosmic-phase/",
  "summary_short": "`inductive` declaration in `TauLib.BookV.Cosmology.CosmologicalEndstate`.",
  "declaration_id": "TauLib.BookV.Cosmology.CosmologicalEndstate::CosmicPhase",
  "declaration_slug": "cosmic-phase",
  "kind": "inductive",
  "name": "CosmicPhase",
  "module_name": "TauLib.BookV.Cosmology.CosmologicalEndstate",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cosmological-endstate/",
  "source_line_start": 151,
  "source_line_end": 156,
  "registry_ids": [
    "V.D183"
  ],
  "related_registry_items": [
    {
      "id": "V.D183",
      "title": "Generative and refinement phases",
      "url": "/registry/object/V.D183/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CosmologicalEndstate.lean#L151-L156",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.CosmologicalEndstate",
        "url": "/verify/taulib/docs/book-v-cosmology-cosmological-endstate/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CosmologicalEndstate.lean#L151-L156",
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

- Module: [TauLib.BookV.Cosmology.CosmologicalEndstate](/verify/taulib/docs/book-v-cosmology-cosmological-endstate/)
- Source path: [`TauLib/BookV/Cosmology/CosmologicalEndstate.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CosmologicalEndstate.lean#L151-L156)
- Source range: L151-L156
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- `V.D183` — Generative and refinement phases

## Immediate Comment / Docstring

```lean
/-- [V.D183] The two cosmic phases.

    1. Generative (α₁ to α_{n_*}): new stable motifs are still created.
       Includes Big Bang, inflation, threshold ladder, astrophysical epochs.
    2. Refinement (α_{n_*} to ∞): no new motifs. Structures settle
       into the absorbing pattern.

    The transition depth n_* is where the last new stable motif
    appears. -/
```

## Source Excerpt

```lean
inductive CosmicPhase where
  /-- Generative: new motifs being created. -/
  | Generative
  /-- Refinement: settling into absorbing pattern. -/
  | Refinement
  deriving Repr, DecidableEq, BEq
```
