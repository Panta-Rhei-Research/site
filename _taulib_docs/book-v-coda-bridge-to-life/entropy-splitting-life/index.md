---
{
  "projection_kind": "taulib_declaration",
  "title": "EntropySplittingLife",
  "permalink": "/verify/taulib/docs/book-v-coda-bridge-to-life/entropy-splitting-life/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Coda.BridgeToLife`.",
  "declaration_id": "TauLib.BookV.Coda.BridgeToLife::EntropySplittingLife",
  "declaration_slug": "entropy-splitting-life",
  "kind": "structure",
  "name": "EntropySplittingLife",
  "module_name": "TauLib.BookV.Coda.BridgeToLife",
  "module_url": "/verify/taulib/docs/book-v-coda-bridge-to-life/",
  "source_line_start": 482,
  "source_line_end": 491,
  "registry_ids": [
    "V.P117"
  ],
  "related_registry_items": [
    {
      "id": "V.P117",
      "title": "Entropy splitting and life",
      "url": "/registry/object/V.P117/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/BridgeToLife.lean#L482-L491",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Coda.BridgeToLife",
        "url": "/verify/taulib/docs/book-v-coda-bridge-to-life/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/BridgeToLife.lean#L482-L491",
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

- Module: [TauLib.BookV.Coda.BridgeToLife](/verify/taulib/docs/book-v-coda-bridge-to-life/)
- Source path: [`TauLib/BookV/Coda/BridgeToLife.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/BridgeToLife.lean#L482-L491)
- Source range: L482-L491
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.P117` — Entropy splitting and life

## Immediate Comment / Docstring

```lean
/-- [V.P117] Entropy splitting and life: a living system maintains
    bounded S_def locally while environment S_def increases.

    - Second Law applies globally, not locally
    - Life = local S_def bounded + global S_def increasing
    - Requires entropy splitting S = S_def + S_ref (X2 from V.D190)
    - The boundary between local and global is the organism boundary -/
```

## Source Excerpt

```lean
structure EntropySplittingLife where
  /-- Local S_def is bounded. -/
  local_bounded : Bool := true
  /-- Global S_def increases. -/
  global_increasing : Bool := true
  /-- Requires entropy splitting. -/
  requires_splitting : Bool := true
  /-- Entropy components (S_def + S_ref). -/
  entropy_components : Nat := 2
  deriving Repr
```
