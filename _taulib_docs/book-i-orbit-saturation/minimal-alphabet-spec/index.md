---
{
  "projection_kind": "taulib_declaration",
  "title": "MinimalAlphabetSpec",
  "permalink": "/corpus/taulib/docs/book-i-orbit-saturation/minimal-alphabet-spec/",
  "summary_short": "`structure` declaration in `TauLib.BookI.Orbit.Saturation`.",
  "declaration_id": "TauLib.BookI.Orbit.Saturation::MinimalAlphabetSpec",
  "declaration_slug": "minimal-alphabet-spec",
  "kind": "structure",
  "name": "MinimalAlphabetSpec",
  "module_name": "TauLib.BookI.Orbit.Saturation",
  "module_url": "/corpus/taulib/docs/book-i-orbit-saturation/",
  "source_line_start": 98,
  "source_line_end": 110,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Saturation.lean#L98-L110",
  "formal_status": "defined",
  "declaration_role": "type/data schema",
  "formal_status_label": "type/data schema",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Orbit.Saturation",
        "url": "/corpus/taulib/docs/book-i-orbit-saturation/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Saturation.lean#L98-L110",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
      "role": "type/data schema",
      "status": "type/data schema"
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

- Module: [TauLib.BookI.Orbit.Saturation](/corpus/taulib/docs/book-i-orbit-saturation/)
- Source path: [`TauLib/BookI/Orbit/Saturation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Saturation.lean#L98-L110)
- Source range: L98-L110
- Kind: `structure`
- Public role: `type/data schema`
- Formal status hint: `type/data schema`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The Minimal Alphabet specification: what 5 generators achieve. -/
```

## Source Excerpt

```lean
structure MinimalAlphabetSpec where
  /-- Ladder completeness: all 3 rewiring levels have channels -/
  add_has_channel : ladderChannel .add_level = some Generator.pi
  mul_has_channel : ladderChannel .mul_level = some Generator.gamma
  exp_has_channel : ladderChannel .exp_level = some Generator.eta
  /-- Saturation: the next level (tetration) has no channel -/
  tet_no_channel : ladderChannel .tet_level = none
  /-- Exactly 3 solenoidal generators -/
  solenoidal_exact : solenoidalGenerators.length = 3
  /-- Channels are pairwise distinct -/
  channels_distinct : Generator.pi ≠ Generator.gamma ∧
                      Generator.pi ≠ Generator.eta ∧
                      Generator.gamma ≠ Generator.eta
```
