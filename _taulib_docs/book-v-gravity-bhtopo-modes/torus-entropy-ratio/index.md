---
{
  "projection_kind": "taulib_declaration",
  "title": "torus_entropy_ratio",
  "permalink": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/torus-entropy-ratio/",
  "summary_short": "`def` declaration in `TauLib.BookV.Gravity.BHTopoModes`.",
  "declaration_id": "TauLib.BookV.Gravity.BHTopoModes::torus_entropy_ratio",
  "declaration_slug": "torus-entropy-ratio",
  "kind": "def",
  "name": "torus_entropy_ratio",
  "module_name": "TauLib.BookV.Gravity.BHTopoModes",
  "module_url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/",
  "source_line_start": 169,
  "source_line_end": 170,
  "registry_ids": [
    "V.P125"
  ],
  "related_registry_items": [
    {
      "id": "V.P125",
      "title": "T² Entropy = π·ι_τ × S² Entropy",
      "url": "/registry/object/V.P125/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/BHTopoModes.lean#L169-L170",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Gravity.BHTopoModes",
        "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/BHTopoModes.lean#L169-L170",
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

- Module: [TauLib.BookV.Gravity.BHTopoModes](/verify/taulib/docs/book-v-gravity-bhtopo-modes/)
- Source path: [`TauLib/BookV/Gravity/BHTopoModes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/BHTopoModes.lean#L169-L170)
- Source range: L169-L170
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `V.P125` — T² Entropy = π·ι_τ × S² Entropy

## Immediate Comment / Docstring

```lean
/-- T² / S² Bekenstein-Hawking entropy ratio = π · ι_τ.
    Derivation: A_{T²} = 4π²R_S²ι_τ, A_{S²} = 4πR_S²
                S_{T²}/S_{S²} = A_{T²}/A_{S²} = πι_τ ≈ 1.0722.
    [V.P125] -/
```

## Source Excerpt

```lean
def torus_entropy_ratio : Float :=
  3.14159265358979 * iota_float
```
