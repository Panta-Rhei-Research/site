---
{
  "projection_kind": "taulib_declaration",
  "title": "resolution_halving_check",
  "permalink": "/verify/taulib/docs/book-ii-transcendentals-iota-tau-confirmed/resolution-halving-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Transcendentals.IotaTauConfirmed`.",
  "declaration_id": "TauLib.BookII.Transcendentals.IotaTauConfirmed::resolution_halving_check",
  "declaration_slug": "resolution-halving-check",
  "kind": "def",
  "name": "resolution_halving_check",
  "module_name": "TauLib.BookII.Transcendentals.IotaTauConfirmed",
  "module_url": "/verify/taulib/docs/book-ii-transcendentals-iota-tau-confirmed/",
  "source_line_start": 145,
  "source_line_end": 154,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/IotaTauConfirmed.lean#L145-L154",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Transcendentals.IotaTauConfirmed",
        "url": "/verify/taulib/docs/book-ii-transcendentals-iota-tau-confirmed/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/IotaTauConfirmed.lean#L145-L154",
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

- Module: [TauLib.BookII.Transcendentals.IotaTauConfirmed](/verify/taulib/docs/book-ii-transcendentals-iota-tau-confirmed/)
- Source path: [`TauLib/BookII/Transcendentals/IotaTauConfirmed.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/IotaTauConfirmed.lean#L145-L154)
- Source range: L145-L154
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Resolution ratio: P_{k+1}/P_k = p_{k+1} >= 2.
    Each refinement step at least halves the resolution. -/
```

## Source Excerpt

```lean
def resolution_halving_check (stages : TauIdx) : Bool :=
  go 1 (stages + 1)
where
  go (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > stages then true
    else
      let pk := primorial k
      pk > 0 && primorial (k + 1) / pk >= 2 && go (k + 1) (fuel - 1)
  termination_by fuel
```
