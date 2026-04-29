---
{
  "projection_kind": "taulib_declaration",
  "title": "constant_entropy_mono",
  "permalink": "/verify/taulib/docs/book-v-cosmology-no-shrink-extended/constant-entropy-mono/",
  "summary_short": "`def` declaration in `TauLib.BookV.Cosmology.NoShrinkExtended`.",
  "declaration_id": "TauLib.BookV.Cosmology.NoShrinkExtended::constant_entropy_mono",
  "declaration_slug": "constant-entropy-mono",
  "kind": "def",
  "name": "constant_entropy_mono",
  "module_name": "TauLib.BookV.Cosmology.NoShrinkExtended",
  "module_url": "/verify/taulib/docs/book-v-cosmology-no-shrink-extended/",
  "source_line_start": 302,
  "source_line_end": 318,
  "registry_ids": [
    "V.P191",
    "V.R472"
  ],
  "related_registry_items": [
    {
      "id": "V.P191",
      "title": "Page Curve Analog: Saturation at Permanence",
      "url": "/registry/object/V.P191/"
    },
    {
      "id": "V.R472",
      "title": "V.OP6 Status: PARTIAL-IMPROVED",
      "url": "/registry/object/V.R472/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/NoShrinkExtended.lean#L302-L318",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.NoShrinkExtended",
        "url": "/verify/taulib/docs/book-v-cosmology-no-shrink-extended/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/NoShrinkExtended.lean#L302-L318",
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

- Module: [TauLib.BookV.Cosmology.NoShrinkExtended](/verify/taulib/docs/book-v-cosmology-no-shrink-extended/)
- Source path: [`TauLib/BookV/Cosmology/NoShrinkExtended.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/NoShrinkExtended.lean#L302-L318)
- Source range: L302-L318
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `V.P191` — Page Curve Analog: Saturation at Permanence
- `V.R472` — V.OP6 Status: PARTIAL-IMPROVED

## Immediate Comment / Docstring

```lean
/-- Example ontic entropy monotonicity: constant entropy (simplest case). -/
```

## Source Excerpt

```lean
def constant_entropy_mono : OnticEntropyMonotonicity where
  maturity_depth := 200
  entropy_at := fun _ => 42
  mono := fun _ => le_refl 42

-- [V.P191] Page Curve Analog: Saturation at Permanence.
-- Pre-maturity: entanglement entropy increases.
-- Post-maturity: saturates at permanence hallmark value.
-- No subsequent decrease (ontic mass non-decreasing).
-- Scope: conjectural (explicit H_∂ spectral decomposition needed).

-- [V.R472] V.OP6 Status: PARTIAL-IMPROVED.
-- Readout entropy bound shows readout cannot carry full ontic info.
-- Ontic entropy mono shows state purifies (opposite of info loss).
-- Page curve analog replaces rise-and-fall with saturation.

end Tau.BookV.Cosmology
```
