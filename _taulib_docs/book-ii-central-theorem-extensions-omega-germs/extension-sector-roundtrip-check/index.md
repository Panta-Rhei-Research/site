---
{
  "projection_kind": "taulib_declaration",
  "title": "extension_sector_roundtrip_check",
  "permalink": "/verify/taulib/docs/book-ii-central-theorem-extensions-omega-germs/extension-sector-roundtrip-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.CentralTheorem.ExtensionsOmegaGerms`.",
  "declaration_id": "TauLib.BookII.CentralTheorem.ExtensionsOmegaGerms::extension_sector_roundtrip_check",
  "declaration_slug": "extension-sector-roundtrip-check",
  "kind": "def",
  "name": "extension_sector_roundtrip_check",
  "module_name": "TauLib.BookII.CentralTheorem.ExtensionsOmegaGerms",
  "module_url": "/verify/taulib/docs/book-ii-central-theorem-extensions-omega-germs/",
  "source_line_start": 242,
  "source_line_end": 260,
  "registry_ids": [
    "II.T38"
  ],
  "related_registry_items": [
    {
      "id": "II.T38",
      "title": "Extensions Are Omega-Germ Transformers",
      "url": "/registry/object/II.T38/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/ExtensionsOmegaGerms.lean#L242-L260",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.CentralTheorem.ExtensionsOmegaGerms",
        "url": "/verify/taulib/docs/book-ii-central-theorem-extensions-omega-germs/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/ExtensionsOmegaGerms.lean#L242-L260",
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

- Module: [TauLib.BookII.CentralTheorem.ExtensionsOmegaGerms](/verify/taulib/docs/book-ii-central-theorem-extensions-omega-germs/)
- Source path: [`TauLib/BookII/CentralTheorem/ExtensionsOmegaGerms.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/ExtensionsOmegaGerms.lean#L242-L260)
- Source range: L242-L260
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.T38` — Extensions Are Omega-Germ Transformers

## Immediate Comment / Docstring

```lean
/-- [II.T38] Full roundtrip including the SectorPair decomposition:
    the bndlift extension, coded as a StageFun, can be recovered from
    its Code/Decode representation. -/
```

## Source Excerpt

```lean
def extension_sector_roundtrip_check (bound db : TauIdx) : Bool :=
  go 2 1 ((bound + 1) * (db + 1))
where
  go (x k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k >= db then go (x + 1) 1 (fuel - 1)
    else
      -- Code the B and C functions separately
      let b_fn : TauIdx -> Int := fun n => (bndlift_stagefun.b_fun n k : Int)
      let c_fn : TauIdx -> Int := fun n => (bndlift_stagefun.c_fun n k : Int)
      let coded_b := code_extract b_fn (k + 1) x
      let coded_c := code_extract c_fn (k + 1) x
      -- Should match the direct evaluation at reduce(x, k+1)
      let direct_b := (bndlift_stagefun.b_fun (reduce x (k + 1)) k : Int)
      let direct_c := (bndlift_stagefun.c_fun (reduce x (k + 1)) k : Int)
      let ok := coded_b == direct_b && coded_c == direct_c
      ok && go x (k + 1) (fuel - 1)
  termination_by fuel
```
