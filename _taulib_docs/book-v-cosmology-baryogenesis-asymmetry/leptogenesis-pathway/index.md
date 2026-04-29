---
{
  "projection_kind": "taulib_declaration",
  "title": "leptogenesis_pathway",
  "permalink": "/verify/taulib/docs/book-v-cosmology-baryogenesis-asymmetry/leptogenesis-pathway/",
  "summary_short": "`def` declaration in `TauLib.BookV.Cosmology.BaryogenesisAsymmetry`.",
  "declaration_id": "TauLib.BookV.Cosmology.BaryogenesisAsymmetry::leptogenesis_pathway",
  "declaration_slug": "leptogenesis-pathway",
  "kind": "def",
  "name": "leptogenesis_pathway",
  "module_name": "TauLib.BookV.Cosmology.BaryogenesisAsymmetry",
  "module_url": "/verify/taulib/docs/book-v-cosmology-baryogenesis-asymmetry/",
  "source_line_start": 193,
  "source_line_end": 197,
  "registry_ids": [
    "V.R375"
  ],
  "related_registry_items": [
    {
      "id": "V.R375",
      "title": "Leptogenesis Pathway: Majorana Neutrinos Enable L→B Conversion",
      "url": "/registry/object/V.R375/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L193-L197",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.BaryogenesisAsymmetry",
        "url": "/verify/taulib/docs/book-v-cosmology-baryogenesis-asymmetry/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L193-L197",
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

- Module: [TauLib.BookV.Cosmology.BaryogenesisAsymmetry](/verify/taulib/docs/book-v-cosmology-baryogenesis-asymmetry/)
- Source path: [`TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L193-L197)
- Source range: L193-L197
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `V.R375` — Leptogenesis Pathway: Majorana Neutrinos Enable L→B Conversion

## Immediate Comment / Docstring

```lean
/-- With Majorana neutrinos (IV.T146), leptogenesis pathway is available. [V.R375]

    Majorana ν → L violation → sphaleron conversion η_L→η_B = (28/79)·η_L.
    Structural reading: σ=C (established) → all 3 ν Majorana → L not conserved.
    The (5/6) prefactor from σ-matrix generation mixing is a conjectural sub-problem.
    (scope: conjectural) -/
```

## Source Excerpt

```lean
def leptogenesis_pathway : String :=
  "Majorana ν (IV.T146, σ=C sprint) → L violation → sphaleron conversion " ++
  "η_L→η_B=(28/79)·η_L (standard sphaleron rate). " ++
  "Structural: (5/6) from σ-matrix generation mixing (conjectural sub-problem). " ++
  "Scope: conjectural (detailed calculation pending)."
```
