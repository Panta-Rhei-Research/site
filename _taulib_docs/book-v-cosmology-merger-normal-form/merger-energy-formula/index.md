---
{
  "projection_kind": "taulib_declaration",
  "title": "merger_energy_formula",
  "permalink": "/verify/taulib/docs/book-v-cosmology-merger-normal-form/merger-energy-formula/",
  "summary_short": "`def` declaration in `TauLib.BookV.Cosmology.MergerNormalForm`.",
  "declaration_id": "TauLib.BookV.Cosmology.MergerNormalForm::merger_energy_formula",
  "declaration_slug": "merger-energy-formula",
  "kind": "def",
  "name": "merger_energy_formula",
  "module_name": "TauLib.BookV.Cosmology.MergerNormalForm",
  "module_url": "/verify/taulib/docs/book-v-cosmology-merger-normal-form/",
  "source_line_start": 374,
  "source_line_end": 377,
  "registry_ids": [
    "V.T224"
  ],
  "related_registry_items": [
    {
      "id": "V.T224",
      "title": "Merger Energy Theorem",
      "url": "/registry/object/V.T224/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/MergerNormalForm.lean#L374-L377",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.MergerNormalForm",
        "url": "/verify/taulib/docs/book-v-cosmology-merger-normal-form/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/MergerNormalForm.lean#L374-L377",
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

- Module: [TauLib.BookV.Cosmology.MergerNormalForm](/verify/taulib/docs/book-v-cosmology-merger-normal-form/)
- Source path: [`TauLib/BookV/Cosmology/MergerNormalForm.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/MergerNormalForm.lean#L374-L377)
- Source range: L374-L377
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `V.T224` — Merger Energy Theorem

## Immediate Comment / Docstring

```lean
/-- [V.T224] Merger energy theorem: non-spinning radiated fraction
    from blueprint fusion. -/
```

## Source Excerpt

```lean
def merger_energy_formula : BlueprintFusionEnergy :=
  ⟨"Non-spinning radiated fraction from blueprint fusion",
   "η = ι_τ² · ν, ν = q/(1+q)²",
   1165⟩
```
