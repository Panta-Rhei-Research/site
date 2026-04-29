---
{
  "projection_kind": "taulib_declaration",
  "title": "five_gen_spec",
  "permalink": "/verify/taulib/docs/book-i-orbit-saturation/five-gen-spec/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Orbit.Saturation`.",
  "declaration_id": "TauLib.BookI.Orbit.Saturation::five_gen_spec",
  "declaration_slug": "five-gen-spec",
  "kind": "theorem",
  "name": "five_gen_spec",
  "module_name": "TauLib.BookI.Orbit.Saturation",
  "module_url": "/verify/taulib/docs/book-i-orbit-saturation/",
  "source_line_start": 113,
  "source_line_end": 119,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Saturation.lean#L113-L119",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Orbit.Saturation",
        "url": "/verify/taulib/docs/book-i-orbit-saturation/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Saturation.lean#L113-L119",
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

- Module: [TauLib.BookI.Orbit.Saturation](/verify/taulib/docs/book-i-orbit-saturation/)
- Source path: [`TauLib/BookI/Orbit/Saturation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Saturation.lean#L113-L119)
- Source range: L113-L119
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The 5-generator system satisfies the Minimal Alphabet specification. -/
```

## Source Excerpt

```lean
theorem five_gen_spec : MinimalAlphabetSpec where
  add_has_channel := rfl
  mul_has_channel := rfl
  exp_has_channel := rfl
  tet_no_channel := rfl
  solenoidal_exact := rfl
  channels_distinct := ⟨by decide, by decide, by decide⟩
```
