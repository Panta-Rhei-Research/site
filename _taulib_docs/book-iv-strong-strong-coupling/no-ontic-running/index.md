---
{
  "projection_kind": "taulib_declaration",
  "title": "NoOnticRunning",
  "permalink": "/verify/taulib/docs/book-iv-strong-strong-coupling/no-ontic-running/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.StrongCoupling`.",
  "declaration_id": "TauLib.BookIV.Strong.StrongCoupling::NoOnticRunning",
  "declaration_slug": "no-ontic-running",
  "kind": "structure",
  "name": "NoOnticRunning",
  "module_name": "TauLib.BookIV.Strong.StrongCoupling",
  "module_url": "/verify/taulib/docs/book-iv-strong-strong-coupling/",
  "source_line_start": 272,
  "source_line_end": 281,
  "registry_ids": [
    "IV.T77"
  ],
  "related_registry_items": [
    {
      "id": "IV.T77",
      "title": "No ontic running --- strong sector",
      "url": "/registry/object/IV.T77/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongCoupling.lean#L272-L281",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Strong.StrongCoupling",
        "url": "/verify/taulib/docs/book-iv-strong-strong-coupling/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongCoupling.lean#L272-L281",
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

- Module: [TauLib.BookIV.Strong.StrongCoupling](/verify/taulib/docs/book-iv-strong-strong-coupling/)
- Source path: [`TauLib/BookIV/Strong/StrongCoupling.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongCoupling.lean#L272-L281)
- Source range: L272-L281
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T77` — No ontic running --- strong sector

## Immediate Comment / Docstring

```lean
/-- [IV.T77] No ontic running in the strong sector:
    alpha_s^* = kappa(C;3) is INDEPENDENT of all regime selectors.
    It is the same element of H_partial regardless of scale, chart,
    or calibration choice.

    Different regime readouts CAN give different numerical values
    (this is what experimentalists call "running"), but the ontic
    coupling itself does not run. Running is a readout phenomenon. -/
```

## Source Excerpt

```lean
structure NoOnticRunning where
  /-- Coupling is regime-independent. -/
  regime_independent : Bool := true
  /-- Same boundary algebra element at all scales. -/
  same_element : Bool := true
  /-- Apparent running is readout artifact. -/
  running_is_readout : Bool := true
  /-- Experimental "running" = different readout charts. -/
  explanation : String := "different regime selectors give different readout values"
  deriving Repr
```
