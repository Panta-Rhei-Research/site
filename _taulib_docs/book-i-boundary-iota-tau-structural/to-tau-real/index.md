---
{
  "projection_kind": "taulib_declaration",
  "title": "CrossingPointDefectGerm.toTauReal",
  "permalink": "/corpus/taulib/docs/book-i-boundary-iota-tau-structural/to-tau-real/",
  "summary_short": "`def` declaration in `TauLib.BookI.Boundary.IotaTauStructural`.",
  "declaration_id": "TauLib.BookI.Boundary.IotaTauStructural::CrossingPointDefectGerm.toTauReal",
  "declaration_slug": "to-tau-real",
  "kind": "def",
  "name": "CrossingPointDefectGerm.toTauReal",
  "module_name": "TauLib.BookI.Boundary.IotaTauStructural",
  "module_url": "/corpus/taulib/docs/book-i-boundary-iota-tau-structural/",
  "source_line_start": 107,
  "source_line_end": 108,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/IotaTauStructural.lean#L107-L108",
  "formal_status": "defined",
  "declaration_role": "definition",
  "formal_status_label": "definition",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.IotaTauStructural",
        "url": "/corpus/taulib/docs/book-i-boundary-iota-tau-structural/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/IotaTauStructural.lean#L107-L108",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "definition",
      "status": "definition"
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

- Module: [TauLib.BookI.Boundary.IotaTauStructural](/corpus/taulib/docs/book-i-boundary-iota-tau-structural/)
- Source path: [`TauLib/BookI/Boundary/IotaTauStructural.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/IotaTauStructural.lean#L107-L108)
- Source range: L107-L108
- Kind: `def`
- Public role: `definition`
- Formal status hint: `definition`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The underlying TauReal of a crossing-point defect germ — its
    operational scalar readout as a Cauchy sequence. -/
```

## Source Excerpt

```lean
def CrossingPointDefectGerm.toTauReal (g : CrossingPointDefectGerm) : TauReal :=
  ⟨g.approx⟩
```
