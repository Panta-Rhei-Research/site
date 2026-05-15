---
{
  "projection_kind": "taulib_declaration",
  "title": "no_hawking_argument",
  "permalink": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/no-hawking-argument/",
  "summary_short": "`def` declaration in `TauLib.BookV.Gravity.BHTopoModes`.",
  "declaration_id": "TauLib.BookV.Gravity.BHTopoModes::no_hawking_argument",
  "declaration_slug": "no-hawking-argument",
  "kind": "def",
  "name": "no_hawking_argument",
  "module_name": "TauLib.BookV.Gravity.BHTopoModes",
  "module_url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/",
  "source_line_start": 183,
  "source_line_end": 187,
  "registry_ids": [
    "V.R374"
  ],
  "related_registry_items": [
    {
      "id": "V.R374",
      "title": "No-Hawking from τ-vacuum: SA-i Forbids Bogoliubov Modes",
      "url": "/registry/object/V.R374/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/BHTopoModes.lean#L183-L187",
  "formal_status": "defined",
  "declaration_role": "docstring/data record",
  "formal_status_label": "docstring/data record",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Gravity.BHTopoModes",
        "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/BHTopoModes.lean#L183-L187",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "docstring/data record",
      "status": "docstring/data record"
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

- Module: [TauLib.BookV.Gravity.BHTopoModes](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/)
- Source path: [`TauLib/BookV/Gravity/BHTopoModes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/BHTopoModes.lean#L183-L187)
- Source range: L183-L187
- Kind: `def`
- Public role: `docstring/data record`
- Formal status hint: `docstring/data record`

## Registry Links

- `V.R374` — No-Hawking from τ-vacuum: SA-i Forbids Bogoliubov Modes

## Immediate Comment / Docstring

```lean
/-- The τ-vacuum has no in/out split → no Bogoliubov transformation
    → no Hawking radiation. SA-i forbids sub-kernel modes.
    Combined with No-Shrink (V.T03): τ-BHs do not evaporate. [V.R374] -/
```

## Source Excerpt

```lean
def no_hawking_argument : String :=
  "τ-BH: vacuum = ℒ = S¹∨S¹ (unique, no in/out split). " ++
  "SA-i forbids sub-coherence-kernel modes. " ++
  "No Bogoliubov transformation → no Hawking radiation. " ++
  "Consistent with No-Shrink (V.T03)."
```
