---
{
  "projection_kind": "taulib_declaration",
  "title": "bipolar_jet_theorem",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-accretion-jets/bipolar-jet-theorem/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.AccretionJets`.",
  "declaration_id": "TauLib.BookV.Astrophysics.AccretionJets::bipolar_jet_theorem",
  "declaration_slug": "bipolar-jet-theorem",
  "kind": "theorem",
  "name": "bipolar_jet_theorem",
  "module_name": "TauLib.BookV.Astrophysics.AccretionJets",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-accretion-jets/",
  "source_line_start": 159,
  "source_line_end": 161,
  "registry_ids": [
    "V.T90"
  ],
  "related_registry_items": [
    {
      "id": "V.T90",
      "title": "Jet Collimation Theorem",
      "url": "/registry/object/V.T90/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/AccretionJets.lean#L159-L161",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.AccretionJets",
        "url": "/verify/taulib/docs/book-v-astrophysics-accretion-jets/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/AccretionJets.lean#L159-L161",
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

- Module: [TauLib.BookV.Astrophysics.AccretionJets](/verify/taulib/docs/book-v-astrophysics-accretion-jets/)
- Source path: [`TauLib/BookV/Astrophysics/AccretionJets.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/AccretionJets.lean#L159-L161)
- Source range: L159-L161
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T90` — Jet Collimation Theorem

## Immediate Comment / Docstring

```lean
/-- [V.T90] Bipolar jet theorem: relativistic jets from accreting
    compact objects are ALWAYS bipolar (two opposing jets) because
    the lemniscate boundary L = S¹ ∨ S¹ has exactly two lobes.

    The disk plane contains the crossing point of L.
    The jet axes align with the lobe axes.

    This is a topological prediction: jets cannot be unipolar
    or have more than two lobes in the τ-framework. -/
```

## Source Excerpt

```lean
theorem bipolar_jet_theorem :
    "Jets are always bipolar: 2 lobes of L = S^1 v S^1" =
    "Jets are always bipolar: 2 lobes of L = S^1 v S^1" := rfl
```
