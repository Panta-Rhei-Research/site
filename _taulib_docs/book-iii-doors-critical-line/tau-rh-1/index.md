---
{
  "projection_kind": "taulib_declaration",
  "title": "tau_rh_1",
  "permalink": "/verify/taulib/docs/book-iii-doors-critical-line/tau-rh-1/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Doors.CriticalLine`.",
  "declaration_id": "TauLib.BookIII.Doors.CriticalLine::tau_rh_1",
  "declaration_slug": "tau-rh-1",
  "kind": "theorem",
  "name": "tau_rh_1",
  "module_name": "TauLib.BookIII.Doors.CriticalLine",
  "module_url": "/verify/taulib/docs/book-iii-doors-critical-line/",
  "source_line_start": 197,
  "source_line_end": 200,
  "registry_ids": [
    "III.D30"
  ],
  "related_registry_items": [
    {
      "id": "III.D30",
      "title": "τ-Effective RH Statement",
      "url": "/registry/object/III.D30/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/CriticalLine.lean#L197-L200",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Doors.CriticalLine",
        "url": "/verify/taulib/docs/book-iii-doors-critical-line/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/CriticalLine.lean#L197-L200",
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

- Module: [TauLib.BookIII.Doors.CriticalLine](/verify/taulib/docs/book-iii-doors-critical-line/)
- Source path: [`TauLib/BookIII/Doors/CriticalLine.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/CriticalLine.lean#L197-L200)
- Source range: L197-L200
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.D30` — τ-Effective RH Statement

## Immediate Comment / Docstring

```lean
/-- [III.D30] Structural: τ-effective RH at depth 1. -/
```

## Source Excerpt

```lean
theorem tau_rh_1 :
    tau_effective_rh_check 1 = true := by native_decide

end Tau.BookIII.Doors
```
