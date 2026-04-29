---
{
  "projection_kind": "taulib_declaration",
  "title": "c_channel_extension_check",
  "permalink": "/verify/taulib/docs/book-ii-central-theorem-hartogs-extension/c-channel-extension-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.CentralTheorem.HartogsExtension`.",
  "declaration_id": "TauLib.BookII.CentralTheorem.HartogsExtension::c_channel_extension_check",
  "declaration_slug": "c-channel-extension-check",
  "kind": "def",
  "name": "c_channel_extension_check",
  "module_name": "TauLib.BookII.CentralTheorem.HartogsExtension",
  "module_url": "/verify/taulib/docs/book-ii-central-theorem-hartogs-extension/",
  "source_line_start": 120,
  "source_line_end": 135,
  "registry_ids": [
    "II.L12"
  ],
  "related_registry_items": [
    {
      "id": "II.L12",
      "title": "Extension in Split-Complex Codomain",
      "url": "/registry/object/II.L12/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/HartogsExtension.lean#L120-L135",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.CentralTheorem.HartogsExtension",
        "url": "/verify/taulib/docs/book-ii-central-theorem-hartogs-extension/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/HartogsExtension.lean#L120-L135",
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

- Module: [TauLib.BookII.CentralTheorem.HartogsExtension](/verify/taulib/docs/book-ii-central-theorem-hartogs-extension/)
- Source path: [`TauLib/BookII/CentralTheorem/HartogsExtension.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/HartogsExtension.lean#L120-L135)
- Source range: L120-L135
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.L12` — Extension in Split-Complex Codomain

## Immediate Comment / Docstring

```lean
/-- [II.L12] Independent C-channel extension: the C-channel of the
    bndlift extension is determined solely by the C-channel of the input. -/
```

## Source Excerpt

```lean
def c_channel_extension_check (bound db : TauIdx) : Bool :=
  go 2 1 ((bound + 1) * (db + 1))
where
  go (x k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k >= db then go (x + 1) 1 (fuel - 1)
    else
      let lifted := bndlift x k
      let chart_lifted := from_tau_idx lifted
      let bp_lifted := interior_bipolar chart_lifted
      let proj_c := SectorPair.mul e_minus_sector bp_lifted
      -- proj_c should have zero B-sector (independence)
      let ok := proj_c.b_sector == 0
      ok && go x (k + 1) (fuel - 1)
  termination_by fuel
```
