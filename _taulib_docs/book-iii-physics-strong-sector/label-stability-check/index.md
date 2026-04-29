---
{
  "projection_kind": "taulib_declaration",
  "title": "label_stability_check",
  "permalink": "/verify/taulib/docs/book-iii-physics-strong-sector/label-stability-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Physics.StrongSector`.",
  "declaration_id": "TauLib.BookIII.Physics.StrongSector::label_stability_check",
  "declaration_slug": "label-stability-check",
  "kind": "def",
  "name": "label_stability_check",
  "module_name": "TauLib.BookIII.Physics.StrongSector",
  "module_url": "/verify/taulib/docs/book-iii-physics-strong-sector/",
  "source_line_start": 71,
  "source_line_end": 86,
  "registry_ids": [
    "III.D43"
  ],
  "related_registry_items": [
    {
      "id": "III.D43",
      "title": "Strong Sector at E₁",
      "url": "/registry/object/III.D43/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/StrongSector.lean#L71-L86",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Physics.StrongSector",
        "url": "/verify/taulib/docs/book-iii-physics-strong-sector/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/StrongSector.lean#L71-L86",
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

- Module: [TauLib.BookIII.Physics.StrongSector](/verify/taulib/docs/book-iii-physics-strong-sector/)
- Source path: [`TauLib/BookIII/Physics/StrongSector.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/StrongSector.lean#L71-L86)
- Source range: L71-L86
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D43` — Strong Sector at E₁

## Immediate Comment / Docstring

```lean
/-- [III.D43] Label stability check: each prime's label is depth-independent. -/
```

## Source Excerpt

```lean
def label_stability_check (bound db : TauIdx) : Bool :=
  go 1 1 ((bound + 1) * (db + 1))
where
  go (i k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if i > bound then true
    else if k > db then go (i + 1) 1 (fuel - 1)
    else
      let p := nth_prime i
      -- Verify label classification against mod-4 residue (not self-comparison)
      let label := label_direct p
      let mod4_ok := if p % 4 == 1 then label == .B
                     else if p % 4 == 3 then label == .C
                     else true
      mod4_ok && go i (k + 1) (fuel - 1)
  termination_by fuel
```
