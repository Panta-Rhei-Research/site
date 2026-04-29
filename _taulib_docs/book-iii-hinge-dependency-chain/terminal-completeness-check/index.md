---
{
  "projection_kind": "taulib_declaration",
  "title": "terminal_completeness_check",
  "permalink": "/verify/taulib/docs/book-iii-hinge-dependency-chain/terminal-completeness-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Hinge.DependencyChain`.",
  "declaration_id": "TauLib.BookIII.Hinge.DependencyChain::terminal_completeness_check",
  "declaration_slug": "terminal-completeness-check",
  "kind": "def",
  "name": "terminal_completeness_check",
  "module_name": "TauLib.BookIII.Hinge.DependencyChain",
  "module_url": "/verify/taulib/docs/book-iii-hinge-dependency-chain/",
  "source_line_start": 203,
  "source_line_end": 217,
  "registry_ids": [
    "III.P30"
  ],
  "related_registry_items": [
    {
      "id": "III.P30",
      "title": "Sector Instantiation Lemma",
      "url": "/registry/object/III.P30/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Hinge/DependencyChain.lean#L203-L217",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Hinge.DependencyChain",
        "url": "/verify/taulib/docs/book-iii-hinge-dependency-chain/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Hinge/DependencyChain.lean#L203-L217",
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

- Module: [TauLib.BookIII.Hinge.DependencyChain](/verify/taulib/docs/book-iii-hinge-dependency-chain/)
- Source path: [`TauLib/BookIII/Hinge/DependencyChain.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Hinge/DependencyChain.lean#L203-L217)
- Source range: L203-L217
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.P30` — Sector Instantiation Lemma

## Immediate Comment / Docstring

```lean
/-- [III.P30] Terminal completeness: the chain covers all four enrichment
    levels. Accumulate which levels appear; verify all 4 are present. -/
```

## Source Excerpt

```lean
def terminal_completeness_check : Bool :=
  go chain_links false false false false (chain_links.length + 1)
where
  go (links : List ChainLink) (e0 e1 e2 e3 : Bool) (fuel : Nat) : Bool :=
    if fuel = 0 then e0 && e1 && e2 && e3
    else match links with
    | [] => e0 && e1 && e2 && e3
    | link :: rest =>
      let lev := link.toEnrLevel
      let e0' := e0 || lev == .E0
      let e1' := e1 || lev == .E1
      let e2' := e2 || lev == .E2
      let e3' := e3 || lev == .E3
      go rest e0' e1' e2' e3' (fuel - 1)
  termination_by fuel
```
