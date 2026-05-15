---
{
  "projection_kind": "taulib_declaration",
  "title": "presheaf_characterization",
  "permalink": "/corpus/taulib/docs/book-i-holomorphy-presheaf-essence/presheaf-characterization/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Holomorphy.PresheafEssence`.",
  "declaration_id": "TauLib.BookI.Holomorphy.PresheafEssence::presheaf_characterization",
  "declaration_slug": "presheaf-characterization",
  "kind": "theorem",
  "name": "presheaf_characterization",
  "module_name": "TauLib.BookI.Holomorphy.PresheafEssence",
  "module_url": "/corpus/taulib/docs/book-i-holomorphy-presheaf-essence/",
  "source_line_start": 82,
  "source_line_end": 84,
  "registry_ids": [
    "I.T40"
  ],
  "related_registry_items": [
    {
      "id": "I.T40",
      "title": "Presheaf Characterization",
      "url": "/registry/object/I.T40/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/PresheafEssence.lean#L82-L84",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Holomorphy.PresheafEssence",
        "url": "/corpus/taulib/docs/book-i-holomorphy-presheaf-essence/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/PresheafEssence.lean#L82-L84",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookI.Holomorphy.PresheafEssence](/corpus/taulib/docs/book-i-holomorphy-presheaf-essence/)
- Source path: [`TauLib/BookI/Holomorphy/PresheafEssence.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/PresheafEssence.lean#L82-L84)
- Source range: L82-L84
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `I.T40` — Presheaf Characterization

## Immediate Comment / Docstring

```lean
/-- [I.T40] Every τ-holomorphic function is a natural transformation
    of the primorial presheaf. -/
```

## Source Excerpt

```lean
theorem presheaf_characterization (hf : HolFun) :
    IsNatTrans hf.transformer.stage_fun :=
  hf.coherent
```
