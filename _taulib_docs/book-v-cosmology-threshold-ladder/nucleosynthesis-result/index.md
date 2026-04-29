---
{
  "projection_kind": "taulib_declaration",
  "title": "NucleosynthesisResult",
  "permalink": "/verify/taulib/docs/book-v-cosmology-threshold-ladder/nucleosynthesis-result/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.ThresholdLadder`.",
  "declaration_id": "TauLib.BookV.Cosmology.ThresholdLadder::NucleosynthesisResult",
  "declaration_slug": "nucleosynthesis-result",
  "kind": "structure",
  "name": "NucleosynthesisResult",
  "module_name": "TauLib.BookV.Cosmology.ThresholdLadder",
  "module_url": "/verify/taulib/docs/book-v-cosmology-threshold-ladder/",
  "source_line_start": 228,
  "source_line_end": 233,
  "registry_ids": [
    "V.T108"
  ],
  "related_registry_items": [
    {
      "id": "V.T108",
      "title": "Nucleosynthesis from tau",
      "url": "/registry/object/V.T108/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/ThresholdLadder.lean#L228-L233",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.ThresholdLadder",
        "url": "/verify/taulib/docs/book-v-cosmology-threshold-ladder/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/ThresholdLadder.lean#L228-L233",
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

- Module: [TauLib.BookV.Cosmology.ThresholdLadder](/verify/taulib/docs/book-v-cosmology-threshold-ladder/)
- Source path: [`TauLib/BookV/Cosmology/ThresholdLadder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/ThresholdLadder.lean#L228-L233)
- Source range: L228-L233
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.T108` — Nucleosynthesis from tau

## Immediate Comment / Docstring

```lean
/-- [V.T108] Nucleosynthesis from τ: the nucleosynthetic window
    produces observed light-element abundances.

    He-4 mass fraction Y_p ~ 0.245 from the neutron-to-proton
    freeze-out ratio at L_N.

    Y_p = 20/81 = 0.24691..., encoded as 246/1000 (floor of 246.913...).
    See HeliumFraction.lean for the full derivation. -/
```

## Source Excerpt

```lean
structure NucleosynthesisResult where
  /-- He-4 mass fraction × 1000. -/
  yp_times_1000 : Nat
  /-- Consistent with observation: Y_p ∈ (0.24, 0.26). -/
  consistent : yp_times_1000 > 240 ∧ yp_times_1000 < 260
  deriving Repr
```
