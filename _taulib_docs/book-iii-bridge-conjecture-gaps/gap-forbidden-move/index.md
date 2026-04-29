---
{
  "projection_kind": "taulib_declaration",
  "title": "gap_forbidden_move",
  "permalink": "/verify/taulib/docs/book-iii-bridge-conjecture-gaps/gap-forbidden-move/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Bridge.ConjectureGaps`.",
  "declaration_id": "TauLib.BookIII.Bridge.ConjectureGaps::gap_forbidden_move",
  "declaration_slug": "gap-forbidden-move",
  "kind": "def",
  "name": "gap_forbidden_move",
  "module_name": "TauLib.BookIII.Bridge.ConjectureGaps",
  "module_url": "/verify/taulib/docs/book-iii-bridge-conjecture-gaps/",
  "source_line_start": 132,
  "source_line_end": 135,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ConjectureGaps.lean#L132-L135",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Bridge.ConjectureGaps",
        "url": "/verify/taulib/docs/book-iii-bridge-conjecture-gaps/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ConjectureGaps.lean#L132-L135",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
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

- Module: [TauLib.BookIII.Bridge.ConjectureGaps](/verify/taulib/docs/book-iii-bridge-conjecture-gaps/)
- Source path: [`TauLib/BookIII/Bridge/ConjectureGaps.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ConjectureGaps.lean#L132-L135)
- Source range: L132-L135
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D113` — Forbidden Move Mapping

## Immediate Comment / Docstring

```lean
/-- [III.D113] All three gaps map to the same forbidden move:
    exponential_quantification (K4 violation). The passage from
    finite verification to infinite proof requires quantifying
    over exponentially many objects. -/
```

## Source Excerpt

```lean
def gap_forbidden_move : AdditiveConjecture → ForbiddenMove
  | .goldbach    => .exponential_quantification
  | .twin_primes => .exponential_quantification
  | .abc         => .exponential_quantification
```
