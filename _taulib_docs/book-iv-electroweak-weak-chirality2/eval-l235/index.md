---
{
  "projection_kind": "taulib_declaration",
  "title": "eval at L235",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-weak-chirality2/eval-l235/",
  "summary_short": "`eval` declaration in `TauLib.BookIV.Electroweak.WeakChirality2`.",
  "declaration_id": "TauLib.BookIV.Electroweak.WeakChirality2::#eval:235",
  "declaration_slug": "eval-l235",
  "kind": "eval",
  "name": null,
  "module_name": "TauLib.BookIV.Electroweak.WeakChirality2",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-weak-chirality2/",
  "source_line_start": 235,
  "source_line_end": 235,
  "registry_ids": [
    "IV.R28",
    "IV.R380",
    "IV.R382",
    "IV.R383"
  ],
  "related_registry_items": [
    {
      "id": "IV.R28",
      "title": "CP Violation and the Crossing Phase",
      "url": "/registry/object/IV.R28/"
    },
    {
      "id": "IV.R380",
      "title": "Physical consequence",
      "url": "/registry/object/IV.R380/"
    },
    {
      "id": "IV.R382",
      "title": "Mass hierarchy: M_Z > M_W",
      "url": "/registry/object/IV.R382/"
    },
    {
      "id": "IV.R383",
      "title": "Definition versus theorem",
      "url": "/registry/object/IV.R383/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakChirality2.lean#L235-L235",
  "formal_status": "computed",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.WeakChirality2",
        "url": "/verify/taulib/docs/book-iv-electroweak-weak-chirality2/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakChirality2.lean#L235-L235",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "eval",
      "status": "computed"
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

- Module: [TauLib.BookIV.Electroweak.WeakChirality2](/verify/taulib/docs/book-iv-electroweak-weak-chirality2/)
- Source path: [`TauLib/BookIV/Electroweak/WeakChirality2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakChirality2.lean#L235-L235)
- Source range: L235-L235
- Kind: `eval`
- Formal status hint: `computed`

## Registry Links

- `IV.R28` — CP Violation and the Crossing Phase
- `IV.R380` — Physical consequence
- `IV.R382` — Mass hierarchy: M_Z > M_W
- `IV.R383` — Definition versus theorem

## Immediate Comment / Docstring

```lean
-- [IV.R28] Chirality is a boundary-character property: it is determined
-- by the sigma-involution acting on boundary characters of L, not by
-- an externally imposed "handedness" label.
-- (Structural remark)

-- [IV.R380] Parity violation is a tau-effective prediction: it follows
-- from the balanced polarity of the A-sector, which is determined by
-- iota_tau. No free parameter is tuned to match experiment.
-- (Structural remark)

-- [IV.R382] No right-handed neutrinos in minimal tau: since neutrinos
-- couple only via the weak (A) sector, and only left-handed states
-- are sigma_A-admissible, right-handed neutrinos do not participate
-- in any interaction within the minimal tau framework.
-- (Structural remark)

-- [IV.R383] CP violation from sigma-polarity involution: the combined
-- action of charge conjugation (C) and parity (P) produces a residual
-- phase that is non-trivial in the A-sector. This is the categorical
-- origin of CP violation in the quark and lepton sectors.
-- (Structural remark)

-- ============================================================
-- SMOKE TESTS
-- ============================================================
```

## Source Excerpt

```lean
#eval sigma_a_admissible .Right                -- false
```
