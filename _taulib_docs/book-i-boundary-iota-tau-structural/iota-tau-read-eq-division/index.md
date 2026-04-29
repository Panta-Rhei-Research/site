---
{
  "projection_kind": "taulib_declaration",
  "title": "iota_tau_read_eq_division",
  "permalink": "/verify/taulib/docs/book-i-boundary-iota-tau-structural/iota-tau-read-eq-division/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.IotaTauStructural`.",
  "declaration_id": "TauLib.BookI.Boundary.IotaTauStructural::iota_tau_read_eq_division",
  "declaration_slug": "iota-tau-read-eq-division",
  "kind": "theorem",
  "name": "iota_tau_read_eq_division",
  "module_name": "TauLib.BookI.Boundary.IotaTauStructural",
  "module_url": "/verify/taulib/docs/book-i-boundary-iota-tau-structural/",
  "source_line_start": 176,
  "source_line_end": 179,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/IotaTauStructural.lean#L176-L179",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.IotaTauStructural",
        "url": "/verify/taulib/docs/book-i-boundary-iota-tau-structural/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/IotaTauStructural.lean#L176-L179",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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

- Module: [TauLib.BookI.Boundary.IotaTauStructural](/verify/taulib/docs/book-i-boundary-iota-tau-structural/)
- Source path: [`TauLib/BookI/Boundary/IotaTauStructural.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/IotaTauStructural.lean#L176-L179)
- Source range: L176-L179
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Structural coupling identity**: for any crossing-point defect
    germ, its scalar readout is Cauchy-equivalent to the operational
    `iota_tau := 2 / (π + e)` from Wave 4.

    This is the H3 structural identity reduced to the operational
    layer Wave 4 already proved.  The deeper paper-level claim that
    `Read(Δ_ω)` is *uniquely determined* by σ-fixedness + crossing-
    point-ness is the universality theorem (deferred to a future
    wave); what we land here is the bridge between the structural
    `Read` and the operational `iota_tau`. -/
```

## Source Excerpt

```lean
theorem iota_tau_read_eq_division (g : CrossingPointDefectGerm)
    (h : IsCrossingPoint g) :
    TauReal.equiv (Read g) TauReal.iota_tau :=
  h.2
```
