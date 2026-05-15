---
{
  "projection_kind": "taulib_declaration",
  "title": "majorana_phases",
  "permalink": "/corpus/taulib/docs/book-iv-electroweak-neutrino-mode/majorana-phases/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Electroweak.NeutrinoMode`.",
  "declaration_id": "TauLib.BookIV.Electroweak.NeutrinoMode::majorana_phases",
  "declaration_slug": "majorana-phases",
  "kind": "theorem",
  "name": "majorana_phases",
  "module_name": "TauLib.BookIV.Electroweak.NeutrinoMode",
  "module_url": "/corpus/taulib/docs/book-iv-electroweak-neutrino-mode/",
  "source_line_start": 259,
  "source_line_end": 260,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L259-L260",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.NeutrinoMode",
        "url": "/corpus/taulib/docs/book-iv-electroweak-neutrino-mode/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L259-L260",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookIV.Electroweak.NeutrinoMode](/corpus/taulib/docs/book-iv-electroweak-neutrino-mode/)
- Source path: [`TauLib/BookIV/Electroweak/NeutrinoMode.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L259-L260)
- Source range: L259-L260
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- If neutrinos are Majorana, there are 2 additional phases.
    Total Majorana phases = N(N-1)/2 = 3 for N = 3. -/
```

## Source Excerpt

```lean
theorem majorana_phases :
    3 * (3 - 1) / 2 = 3 := by omega
```
