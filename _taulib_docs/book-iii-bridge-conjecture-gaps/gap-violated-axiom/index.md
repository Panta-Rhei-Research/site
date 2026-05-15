---
{
  "projection_kind": "taulib_declaration",
  "title": "gap_violated_axiom",
  "permalink": "/corpus/taulib/docs/book-iii-bridge-conjecture-gaps/gap-violated-axiom/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Bridge.ConjectureGaps`.",
  "declaration_id": "TauLib.BookIII.Bridge.ConjectureGaps::gap_violated_axiom",
  "declaration_slug": "gap-violated-axiom",
  "kind": "def",
  "name": "gap_violated_axiom",
  "module_name": "TauLib.BookIII.Bridge.ConjectureGaps",
  "module_url": "/corpus/taulib/docs/book-iii-bridge-conjecture-gaps/",
  "source_line_start": 138,
  "source_line_end": 139,
  "registry_ids": [
    "III.D113"
  ],
  "related_registry_items": [
    {
      "id": "III.D113",
      "title": "Forbidden Move Mapping",
      "url": "/registry/object/III.D113/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ConjectureGaps.lean#L138-L139",
  "formal_status": "defined",
  "declaration_role": "definition",
  "formal_status_label": "definition",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Bridge.ConjectureGaps",
        "url": "/corpus/taulib/docs/book-iii-bridge-conjecture-gaps/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ConjectureGaps.lean#L138-L139",
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

- Module: [TauLib.BookIII.Bridge.ConjectureGaps](/corpus/taulib/docs/book-iii-bridge-conjecture-gaps/)
- Source path: [`TauLib/BookIII/Bridge/ConjectureGaps.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ConjectureGaps.lean#L138-L139)
- Source range: L138-L139
- Kind: `def`
- Public role: `definition`
- Formal status hint: `definition`

## Registry Links

- `III.D113` — Forbidden Move Mapping

## Immediate Comment / Docstring

```lean
/-- [III.D113] The violated axiom for all three gaps is K4. -/
```

## Source Excerpt

```lean
def gap_violated_axiom (c : AdditiveConjecture) : ChainLink :=
  violated_axiom (gap_forbidden_move c)
```
