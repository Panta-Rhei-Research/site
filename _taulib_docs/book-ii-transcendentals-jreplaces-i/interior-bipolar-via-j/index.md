---
{
  "projection_kind": "taulib_declaration",
  "title": "interior_bipolar_via_j",
  "permalink": "/verify/taulib/docs/book-ii-transcendentals-jreplaces-i/interior-bipolar-via-j/",
  "summary_short": "`def` declaration in `TauLib.BookII.Transcendentals.JReplacesI`.",
  "declaration_id": "TauLib.BookII.Transcendentals.JReplacesI::interior_bipolar_via_j",
  "declaration_slug": "interior-bipolar-via-j",
  "kind": "def",
  "name": "interior_bipolar_via_j",
  "module_name": "TauLib.BookII.Transcendentals.JReplacesI",
  "module_url": "/verify/taulib/docs/book-ii-transcendentals-jreplaces-i/",
  "source_line_start": 131,
  "source_line_end": 146,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/JReplacesI.lean#L131-L146",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Transcendentals.JReplacesI",
        "url": "/verify/taulib/docs/book-ii-transcendentals-jreplaces-i/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/JReplacesI.lean#L131-L146",
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

- Module: [TauLib.BookII.Transcendentals.JReplacesI](/verify/taulib/docs/book-ii-transcendentals-jreplaces-i/)
- Source path: [`TauLib/BookII/Transcendentals/JReplacesI.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/JReplacesI.lean#L131-L146)
- Source range: L131-L146
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Every tau-admissible point inherits bipolar decomposition via j.
    The B-coordinate maps to the e_+-sector, C to e_-. -/
```

## Source Excerpt

```lean
def interior_bipolar_via_j (bound : TauIdx) : Bool :=
  go 2 (bound + 1)
where
  go (x fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else
      let p := from_tau_idx x
      let bp := interior_bipolar p
      -- e_+ projection recovers B-sector
      let proj_plus := SectorPair.mul e_plus_sector bp
      let proj_minus := SectorPair.mul e_minus_sector bp
      -- Sum recovers full bipolar pair
      (SectorPair.add proj_plus proj_minus == bp) &&
      go (x + 1) (fuel - 1)
  termination_by fuel
```
