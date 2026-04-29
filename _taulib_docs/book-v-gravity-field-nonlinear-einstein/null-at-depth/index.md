---
{
  "projection_kind": "taulib_declaration",
  "title": "NullAtDepth",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-nonlinear-einstein/null-at-depth/",
  "summary_short": "`structure` declaration in `TauLib.BookV.GravityField.NonlinearEinstein`.",
  "declaration_id": "TauLib.BookV.GravityField.NonlinearEinstein::NullAtDepth",
  "declaration_slug": "null-at-depth",
  "kind": "structure",
  "name": "NullAtDepth",
  "module_name": "TauLib.BookV.GravityField.NonlinearEinstein",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-nonlinear-einstein/",
  "source_line_start": 206,
  "source_line_end": 217,
  "registry_ids": [
    "V.D58"
  ],
  "related_registry_items": [
    {
      "id": "V.D58",
      "title": "Null intertwiner",
      "url": "/registry/object/V.D58/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/NonlinearEinstein.lean#L206-L217",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.NonlinearEinstein",
        "url": "/verify/taulib/docs/book-v-gravity-field-nonlinear-einstein/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/NonlinearEinstein.lean#L206-L217",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
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

- Module: [TauLib.BookV.GravityField.NonlinearEinstein](/verify/taulib/docs/book-v-gravity-field-nonlinear-einstein/)
- Source path: [`TauLib/BookV/GravityField/NonlinearEinstein.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/NonlinearEinstein.lean#L206-L217)
- Source range: L206-L217
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D58` — Null intertwiner

## Immediate Comment / Docstring

```lean
/-- [V.D58] Null intertwiner at depth n: a photon-like boundary
    transport mode resolved at a specific refinement depth.

    The null condition at depth n determines the local light cone
    and hence the causal structure at that resolution. -/
```

## Source Excerpt

```lean
structure NullAtDepth where
  /-- Refinement depth. -/
  depth : Nat
  /-- Depth positive. -/
  depth_pos : depth > 0
  /-- Sector (must be B = EM). -/
  sector : Sector := .B
  /-- Null selects EM. -/
  sector_is_em : sector = .B := by rfl
  /-- Speed is c at this depth. -/
  speed_is_c : Bool := true
  deriving Repr
```
