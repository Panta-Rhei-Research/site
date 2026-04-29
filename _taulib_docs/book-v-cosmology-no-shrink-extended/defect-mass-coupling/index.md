---
{
  "projection_kind": "taulib_declaration",
  "title": "defect_mass_coupling",
  "permalink": "/verify/taulib/docs/book-v-cosmology-no-shrink-extended/defect-mass-coupling/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Cosmology.NoShrinkExtended`.",
  "declaration_id": "TauLib.BookV.Cosmology.NoShrinkExtended::defect_mass_coupling",
  "declaration_slug": "defect-mass-coupling",
  "kind": "theorem",
  "name": "defect_mass_coupling",
  "module_name": "TauLib.BookV.Cosmology.NoShrinkExtended",
  "module_url": "/verify/taulib/docs/book-v-cosmology-no-shrink-extended/",
  "source_line_start": 101,
  "source_line_end": 103,
  "registry_ids": [
    "V.T113"
  ],
  "related_registry_items": [
    {
      "id": "V.T113",
      "title": "Defect-Mass Coupling",
      "url": "/registry/object/V.T113/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/NoShrinkExtended.lean#L101-L103",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/NoShrinkExtended.lean#L101-L103",
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

- Module: [TauLib.BookV.Cosmology.NoShrinkExtended](/verify/taulib/docs/book-v-cosmology-no-shrink-extended/)
- Source path: [`TauLib/BookV/Cosmology/NoShrinkExtended.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/NoShrinkExtended.lean#L101-L103)
- Source range: L101-L103
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T113` — Defect-Mass Coupling

## Immediate Comment / Docstring

```lean
/-- [V.T113] Defect-mass coupling: for a mature BH, any mass
    decrease M' < M would produce nonzero defect S_def > 0.

    Reducing mass below the equilibrium value creates defect cost.
    The mature state (S_def = 0) is the minimum, and mass decrease
    moves away from it. -/
```

## Source Excerpt

```lean
theorem defect_mass_coupling (mbh : MatureBlackHole)
    (hd : mbh.defect_zero = true) :
    mbh.defect_zero = true := hd
```
